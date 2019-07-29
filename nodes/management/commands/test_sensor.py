from django.core.management.base import BaseCommand, CommandError
from nodes.sensors.sense_hat import SenseHAT
from nodes.sensors.dht11 import DHT11


class Command(BaseCommand):
    help = 'Tests the some sensor class'

    def write(self, val):
        if val:
            self.stdout.write(val)
        else:
            self.stdout.write('no value given')

    def handle(self, *args, **options):
        try:
            s = SenseHAT()
            self.write(s.test_me())
            data = s.get_data()
            self.write(data)


        except Exception as e:
            print(e.__repr__())

        s2 = DHT11()
        self.write(s2.test_me())
        self.write(s2.get_data())
