from importlib import import_module
from .base_sensor import BaseSensor

"""
Try to load the following classes.
This may fail, as some specific dependencies are not available to all systems.
"""
SENSOR_CLASSES = [
    ('Stub', '.stub'),
    ('DHT22', '.dht22'),
    ('BME280', '.bme280'),
    ('SenseHAT', '.sense_hat'),
]

PROTOCOL_GPIO = 'GPIO'
PROTOCOL_I2C = 'I²C'
PROTOCOL_CHOICES = [
    ('GPIO', PROTOCOL_GPIO),
    ('I2C', PROTOCOL_I2C),
]

# List of sensors incompatible with this system
INCOMPATIBLE_SENSOR_CLASSES = []

for name, path in SENSOR_CLASSES:
    try:
        module = import_module(path, package='nodes.sensors')
    except ImportError:
        INCOMPATIBLE_SENSOR_CLASSES.append((name, path))

# List of sensors that are available for this system
SENSOR_CHOICES = [(cls.__name__, cls.__name__) for cls in BaseSensor.__subclasses__()]

# Sensors unavailable are marked with an asterisk
for name, path in INCOMPATIBLE_SENSOR_CLASSES:
    SENSOR_CHOICES.append((name, name + '*'))
