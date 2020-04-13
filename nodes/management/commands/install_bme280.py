from django.core.management.base import BaseCommand
from nodes.management.commands._utils import CommandUtils


class Command(BaseCommand):
    help = 'Install libraries to use the BME280 sensor'

    def handle(self, *args, **options):
        utils = CommandUtils(self)
        utils.write('Installing libraries for BME280...')
        utils.apt_install('python-smbus i2c-tools')
        utils.success('BME280 installed successfully! You  may need to reboot.')
