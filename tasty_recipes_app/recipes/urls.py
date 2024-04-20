"""
http://localhost:8000/recipe/catalogue/ - Catalogue page
http://localhost:8000/recipe/create/ - Recipe create page
http://localhost:8000/recipe/1/details/ - Recipe details page
http://localhost:8000/recipe/1/edit/ - Recipe edit page
http://localhost:8000/recipe/1/delete/ - Recipe delete page
"""
from django.urls import path

from tasty_recipes_app.recipes.views import catalogue, recipe_create, recipe_details, recipe_edit, recipe_delete

urlpatterns = (
    path("catalogue/", catalogue, name="catalogue"),
    path("create/", recipe_create, name="recipe_create"),
    path("<int:pk>/details/", recipe_details, name="recipe_details"),
    path("<int:pk>/edit/", recipe_edit, name="recipe_edit"),
    path("<int:pk>/delete/", recipe_delete, name="recipe_delete"),
)