from .base_sensor import BaseSensor

class DHT11(BaseSensor):
    """
    Used to read data from a DHT11 sensor
    """
    name = 'DHT11'
    
    def _read_data(self):
        return '{"temp": 35, "humid": 50}'

