from django.core.management.base import BaseCommand
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

        s2 = DHT11()
        utils.write(s2.test_me())
        utils.write(s2.get_data())
