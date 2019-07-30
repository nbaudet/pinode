from decimal import Decimal, ROUND_HALF_UP
import json
from .base_sensor import BaseSensor
from sense_hat import SenseHat


class SenseHAT(BaseSensor):
    """
    Used to read data from the Sense HAT board's sensors

    Please read following documentation to install and activate
    necessary kernel modules on your Raspberry Pi.
    Documentation:
    https://pythonhosted.org/sense-hat/

    Steps from the documentation:
    1) Ensure APT package list is up-to-date:
    `$ sudo apt-get update`
    2) Install the sense-hat package which will:
        - ensure the kernel is up-to-date
        - enable I2C
        - install the necessary libraries and programs
    `$ sudo apt-get install sense-hat`
    3) If I2C was not available, it is necessary to reboot:
    `$ sudo reboot`
    """

    name = 'SenseHAT'

    def round(self, float_number):
        return Decimal(float_number).quantize(Decimal('1.0'), rounding=ROUND_HALF_UP)

    def _read_data(self):
        sense = SenseHat()
        # sense.show_message('Hello world!')

        # Float, the percentage of relative humidity
        humid = self.round(sense.get_humidity())

        # Float, the current temperature in degrees Celsius
        temp_h = self.round(sense.get_temperature_from_humidity())

        # Other way to get the temperature from the Sense HAT
        temp_p = self.round(sense.get_temperature_from_pressure())

        # Float, the current pressure in Millibars
        press = self.round(sense.get_pressure())

        data = {
            "temp_humidity": str(temp_h),
            "temp_pressure": str(temp_p),
            "humid": str(humid),
            "press": str(press)
        }

        return json.dumps(data)
