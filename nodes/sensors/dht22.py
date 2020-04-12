from .base_sensor import BaseSensor


class DHT22(BaseSensor):
    """
    Used to read data from a DHT22 (AM2303) sensor
    """

    name = 'DHT22'

    def _read_data(self):

        return '{"temp": 35, "humid": 50}'
