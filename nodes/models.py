from django.db import models
from datetime import datetime
import jsonfield

# Create your models here.
class Node(models.Model):
    mac_address = models.CharField(max_length=25, primary_key=True)
    ip_address = models.GenericIPAddressField()
    name = models.CharField(max_length=50)
    is_self = models.BooleanField()
    is_registered = models.BooleanField(default=False)
    registered_since = models.DateTimeField(
        auto_now_add=True, null=True
    )  # Saves the date of object creation
    last_active = models.DateTimeField(
        auto_now=True
    )  # updated each time the object is changed
    signal_strength = models.DecimalField(
        max_digits=3, decimal_places=1, null=True
    )  # TODO: in percent or neg. dB?
    battery_status = models.DecimalField(
        max_digits=3, decimal_places=1, null=True
    )  # in percent
    is_used = models.BooleanField(default=True)
    info_string = jsonfield.JSONField()

    def delete(self):
        """
        Overrides the delete method to change the is_used boolean to False
        and not lose all data for this Node
        """
        self.is_used = False
        self.save()

    def register(self):
        """
        Register the node to the master
        """
        self.is_registered = True
        self.registered_since = datetime.now()


class Activity(models.Model):
    node = models.ForeignKey('Node', on_delete=models.CASCADE)
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
