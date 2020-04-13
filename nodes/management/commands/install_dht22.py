from django.core.management.base import BaseCommand
from nodes.management.commands._utils import CommandUtils


class Command(BaseCommand):
    help = 'Install libraries to use the DHT22 sensor'

    def handle(self, *args, **options):
        utils = CommandUtils(self)
        utils.write('Installing libraries for DHT22...')
        utils.pip_install('adafruit-circuitpython-dht')
        utils.pip_install('RPi.GPIO')
        utils.apt_install('libgpiod2')
        utils.success('DHT22 installed successfully! You  may need to reboot.')
