from django.contrib import admin

from tasty_recipes_app.recipes.models import Recipe


@admin.register(Recipe)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recipe._meta.fields]
