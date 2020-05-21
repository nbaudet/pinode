import time
import json
import adafruit_dht
import RPi.GPIO as GPIO

from .base_sensor import BaseSensor


class DHT22(BaseSensor):
    """
    Used to read data from a DHT22 (AM2303) sensor
    """

    name = 'DHT22'

    def _read_data(self, config):
        
        dht = adafruit_dht.DHT22(config.pin)
        
        while True:
            try:
                temp = dht.temperature
                humid = dht.humidity
                break
            except RuntimeError as e:
                print('Error:', e)
                time.sleep(2) # Wait before retry
                
        data = {
            "temp": str(temp),
            "humid": str(humid),
        }

        return json.dumps(data)

    def get_protocol(self) -> str:
        return BaseSensor.PROTOCOL_GPIO
