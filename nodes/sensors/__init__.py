from .base_sensor import BaseSensor
from .dht22 import DHT22
from .bme280 import BME280

# TODO: Make an autoimporter wrapped in try block for all subclasses of
# BaseSensor, then change doc in add_sensor.md
# Otherwise, this package will break testing on traditional PC.

"""
Load sensors hereunder when they require a special configuration or module only available in certain environments
like a Raspberry Pi
"""
try:
    from .sense_hat import SenseHAT
except ImportError:
    pass

# List of sensors that are available for this system
SENSOR_CHOICES = [(cls.__name__, cls.__name__) for cls in BaseSensor.__subclasses__()]
