import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def calculate_age(bday):
    today = datetime.date.today()
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    return age

def validate_age(bday):
    age = calculate_age(bday)
    if (age < 18):
        raise ValidationError(
            f"Age {age} is below 18",
            # _('%(value)s is below 18'),
            params={'value': bday},
        )