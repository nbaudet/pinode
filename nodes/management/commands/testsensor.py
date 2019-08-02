from django.core.management.base import BaseCommand
from django.utils import timezone
from nodes.models import Node, Activity
from nodes.sensors.sense_hat import SenseHAT
from nodes.sensors.dht11 import DHT11
from nodes.management.commands._utils import CommandUtils


class Command(BaseCommand):
    help = 'Test your sensor class'

    def handle(self, *args, **options):
        utils = CommandUtils(self)
        s = SenseHAT()
        utils.write(s.test_me())
        data = s.get_data()
        utils.success(data)
        self_node = Node.objects.get(is_self=True)
        Activity.objects.create(node=self_node, datetime=timezone.now(), value=data)

        s2 = DHT11()
        utils.write(s2.test_me())
        utils.write(s2.get_data())
