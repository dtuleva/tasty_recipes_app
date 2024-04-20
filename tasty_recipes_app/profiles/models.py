"""
Profile
- Nickname
    Character field, required, unique.
    It should consist of a maximum of 20 characters.
    It should consist of a minimum of 2 characters.
    Error message: "Nickname must be at least 2 chars long!".
- First Name
    Character field, required.
    It should consist of a maximum of 30 characters.
    The first name must start with a capital letter.
    Error message: "Name must start with a capital letter!".
- Last Name
    Character field, required.
    It should consist of a maximum of 30 characters.
    The last name must start with a capital letter.
    Error message: "Name must start with a capital letter!".
- Chef
    Boolean field, required.
    Default value: False.
- Bio
    Text field, optional.
"""
from django.core import validators, exceptions
from django.db import models


def validate_name_first_letter_capital(value):
    if not value[0].isupper():
        raise exceptions.ValidationError("Name must start with a capital letter!")


class Profile(models.Model):
    NICKNAME_MAX_LEN = 20
    NICKNAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    nickname = models.CharField(
        max_length=NICKNAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(
                limit_value=NICKNAME_MIN_LEN,
                message="Nickname must be at least 2 chars long!",
            ),
        ),
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validate_name_first_letter_capital,
        ),
        verbose_name="First Name",
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validate_name_first_letter_capital,
        ),
        verbose_name="Last Name",
        null=False,
        blank=False,
    )
    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
