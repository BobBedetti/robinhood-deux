from django.core.validators import RegexValidator

from deux import strings

#: Regex validator for phone numbers.
phone_number_validator = RegexValidator(
    regex=r"^(\d{7,15})$",
    message=strings.INVALID_PHONE_NUMBER_ERROR)
