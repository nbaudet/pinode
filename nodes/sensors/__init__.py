from .base_sensor import BaseSensor
from .dht11 import DHT11

"""
Load sensors this way when they require a special configuration or module only available in certain environments
like a Raspberry Pi
"""
try:
    from .sense_hat import SenseHAT
except ImportError:
    pass
