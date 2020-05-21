from abc import ABC, abstractmethod


class BaseSensor(ABC):
    """
    Base class for sensors
    It is used to automatically declare Celery tasks.
    When subclassing BaseSensor, write a concrete implementation
    for _read_data.
    """

    name = 'Give human readable name to the sensor'
    
    def get_data(self, config) -> str:
        """
        Wrapper method of _read_data used for declaring Celery task
        """
        return self._read_data(config)

    @abstractmethod
    def _read_data(self, config) -> str:
        """
        Implementation for concrete reading of the sensor, and
        return sensor data as a JSON string
        """
        raise NotImplementedError

    @abstractmethod
    def get_protocol(self) -> str:
        """
        :return: The protocol used to communicate between the sensor and the node
        """
        raise NotImplementedError

    def test_me(self) -> str:
        return f"Hi, I'm {self.name}"
