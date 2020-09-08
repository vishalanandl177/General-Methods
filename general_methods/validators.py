"""
    File:           validators.py
    Description:    Use the function to validate inputs in models.
"""
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


# Responsible to validate email field
def email_validator(email):
    if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email) is None:
        raise ValidationError(
            _('Invalid email address')
        )


# Responsible to validate mobile number, without country code
def mobile_number_validator(text):
    if re.match("^[6-9][0-9]{9}$", text) is None:
        raise ValidationError(
            _('Invalid mobile number')
        )


# Responsible to validate country code
def country_code_validator(text):
    if re.match("^(\+)[1-9][0-9]?$", text) is None:
        raise ValidationError(
            _('Invalid country code')
        )


# Responsible to validate a string, must have only alphabets or number or space
def string_with_space_validator(text):
    if re.match('^[ a-zA-Z]+$', text) is None:
        raise ValidationError(
            _('Only alphabets and spaces are allowed')
        )
