from django.core.management.base import BaseCommand
from django.utils import timezone
from nodes.models import Node, Activity, Sensor
from nodes.management.commands._utils import CommandUtils


class Command(BaseCommand):
    help = 'Test your sensor class'

    def handle(self, *args, **options):
        utils = CommandUtils(self)
        self_node = Node.objects.get(is_self=True)

        """
        Programmatically import the modules configured on the current device,
        then measure and output the result 
        """
        # List each unique sensor, then make a list of names
        unique_sensors = list(
            Sensor.objects.filter(node=self_node).values('type').distinct()
        )
        unique_sensor_types = []
        for sensor in unique_sensors:
            unique_sensor_types.append(sensor['type'])

        # Programmatically import required sensor classes from names
        if unique_sensor_types:
            module = __import__('nodes.sensors', fromlist=unique_sensor_types)

            # List all sensors configurations on this node
            self_sensors_config = list(Sensor.objects.filter(node=self_node))
            for sensor_config in self_sensors_config:
                sensor_cls = getattr(module, sensor_config.type)
                s = sensor_cls()
                data = s.get_data(sensor_config)
                utils.success(data)
                Activity.objects.create(
                    node=self_node,
                    sensor=sensor_config,
                    datetime=timezone.now(),
                    value=data,
                )
