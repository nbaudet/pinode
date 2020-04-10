from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
import jsonfield


class Node(models.Model):
    name = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=25, blank=True, null=True)
    ip_address = models.GenericIPAddressField()
    is_self = models.BooleanField()
    is_registered = models.BooleanField(default=False)
    registered_since = models.DateTimeField(
        auto_now_add=True, null=True
    )  # Saves the date of object creation
    last_active = models.DateTimeField(
        auto_now=True
    )  # updated each time the object is changed
    signal_strength = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True
    )  # TODO: in percent or neg. dB?
    battery_status = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True
    )  # in percent
    is_soft_deleted = models.BooleanField(default=False)
    info_string = jsonfield.JSONField()

    def delete(self):
        """
        Overrides the delete method to change the is_used boolean to False
        and not lose all data for this Node
        TODO: Evaluate if on_delete=models.SET_NULL() wouldn't be better
        """
        self.is_soft_deleted = True
        self.save()

    def register(self):
        """
        Register the node to the master
        """
        self.is_registered = True
        self.registered_since = datetime.now()

    def get_sensors(self):
        """
        Returns Sensors configured on this Node
        :return: List of Sensors
        """
        return Sensor.objects.filter(node=self)

    def __str__(self):
        is_self = ' - IS_SELF' if self.is_self else ''
        return f'{self.name} @ {self.ip_address}{is_self}'


class Activity(models.Model):
    """
    Stores a sensor activity
    """
    node = models.ForeignKey('Node', on_delete=models.SET_NULL, null=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    # TODO: consider adding 'auto_now_add=True' back after stubs are not needed anymore
    value = jsonfield.JSONField()

    # def save(self, commit=True):
    #     """
    #     Overrides the save method so that we can create some stub data with
    #     stub datetimes passed to the object.
    #     """
    #     super(CallResultTypeForm, self).save(commit=False)
    #     self.datetime = (self.datetime is None) ? datetime.datetime.now : self.datetime
    #     self.save()
    #     return self.instance()


class Sensor(models.Model):
    """
    Stores a Sensor configuration on a Node
    """
    this_node = Node.objects.filter(is_self=True)

    type = models.CharField(
        help_text='If your sensor is not in the list, read the doc to easily add your own.',
        choices=settings.SENSOR_CHOICES,
        max_length=20,
    )
    pin = models.IntegerField(
        help_text='The GPIO pin to which the sensor\'s data cable is connected',
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(40),
            MinValueValidator(1)
        ],
    )
    node = models.ForeignKey(
        'Node',
        help_text='The Node to which this sensor is connected to',
        on_delete=models.SET_NULL,
        null=True,
        default=this_node
    )

    def __str__(self):
        on_node = '' if self.node.is_self else f' on {self.node}'
        return f'{self.type}{on_node} on GPIO pin {self.pin}'
