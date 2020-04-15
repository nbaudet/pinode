from json import dumps

from .base_sensor import BaseSensor
from .libbme280 import readBME280All


class BME280(BaseSensor):
    """
    Used to read data from a BME280 sensor
    Credits of libbme280.py to Matt Hawkins from raspberrypi-spy.co.uk
    """

    name = 'BME280'

    def _read_data(self, config):
        temp, pressure, humid = readBME280All()
                
        data = {
            "temp": f'{temp:.1f}',
            "humid": f'{humid:.1f}',
            "press": f'{pressure:.1f}',
        }

        return dumps(data)
