from abc import ABC, abstractmethod

class BaseSensor(ABC):
    """
    Base class for sensors
    It is used for automatically declaring Celery tasks.
    When subclassing BaseSensor, write a concrete implementation
    for _read_data.
    """
    name = 'Give human readable name to the sensor'

    def get_data(self):
        """
        Wrapper method of _read_data used for declaring Celery task
        """
        return self._read_data()

    @abstractmethod
    def _read_data(self):
        """
        Implementation for concrete reading of the sensor, and
        return sensor data as python dictionary
        """
        raise NotImplementedError

    def test_me(self):
        return 'Hi, I\'m {}'.format(self.name)
