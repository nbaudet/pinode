from json import dumps
from time import sleep

from random import uniform
from .base_sensor import BaseSensor


class Stub(BaseSensor):
    """
    Just a stub class to generate random data, and do tests on systems that do not have GPIO ports.
    """

    name = 'Stub sensor'

    def _read_data(self, config) -> str:
        sleep(0.2)

        data = {
            "temp": f'{uniform(20.0, 28.9):.1f}',
            "humid": f'{uniform(30.0, 39.9):.1f}',
        }

        return dumps(data)

    def get_protocol(self) -> str:
        return BaseSensor.PROTOCOL_GPIO
