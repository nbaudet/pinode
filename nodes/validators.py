from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from nodes.sensors import INCOMPATIBLE_SENSOR_CLASSES


def validate_sensor(value: str):
    # TODO: if we don't add the sensor on the current node, shouldn't do this validation
    if value in dict(INCOMPATIBLE_SENSOR_CLASSES):
        raise ValidationError(
            _('%(value)s is not available on this system'),
            params={'value': value},
        )
