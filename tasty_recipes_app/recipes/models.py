"""
Recipe
- Title
    Character field, required, unique.
    It should consist of a maximum of 100 characters.
    It should consist of a minimum of 10 characters.
- Cuisine Type
    Character (choice) field, required.
    It should consist of a maximum of 7 characters.
    The choices are "French", "Chinese", "Italian", "Balkan" and "Other".
- Ingredients
    Text field, required.
    Help text: "Ingredients must be separated by a comma and space."
- Instructions
    Text field, required.
- Cooking Time
    Positive integer field, required.
    Time cannot be below 1.
    Help text: "Provide the cooking time in minutes."
- Image URL
    URL field, optional.
"""
import enum

from django.core import validators
from django.db import models


class ChoicesEnum(enum.Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_length(cls):
        return max([len(x.name) for x in cls])


class RecipeCuisineType(ChoicesEnum):
    FRENCH = "French"
    CHINESE = "Chinese"
    ITALIAN = "Italian"
    BALKAN = "Balkan"
    OTHER = "Other"


class Recipe(models.Model):
    TITLE_MAX_LEN = 100
    TITLE_MIN_LEN = 10
    COOKING_TIME_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(
            validators.MinLengthValidator(
                limit_value=TITLE_MIN_LEN
            ),
        ),
        unique=True,
        null=False,
        blank=False,
    )
    cuisine_type = models.CharField(
        max_length=RecipeCuisineType.max_length(),
        choices=RecipeCuisineType.choices(),
        verbose_name="Cuisine Type",
        null=False,
        blank=False,
    )
    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
        null=False,
        blank=False,
    )
    instructions = models.TextField(
        null=False,
        blank=False,
    )
    cooking_time = models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes.",
        validators=(
            validators.MinValueValidator(
                limit_value=COOKING_TIME_MIN_VALUE
            ),
        ),
        verbose_name="Cooking Time",
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        verbose_name="Image URL",
        blank=True,
        null=True
    )
