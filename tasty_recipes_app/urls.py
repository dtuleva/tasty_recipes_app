"""
http://localhost:8000/ - Home page
http://localhost:8000/recipe/catalogue/ - Catalogue page
http://localhost:8000/recipe/create/ - Recipe create page
http://localhost:8000/recipe/1/details/ - Recipe details page
http://localhost:8000/recipe/1/edit/ - Recipe edit page
http://localhost:8000/recipe/1/delete/ - Recipe delete page
http://localhost:8000/profile/create/ - Profile create page
http://localhost:8000/profile/details/ - Profile details page
http://localhost:8000/profile/edit/ - Profile edit page
http://localhost:8000/profile/delete/ - Profile delete page
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasty_recipes_app.core.urls")),
    path("recipe/", include("tasty_recipes_app.recipes.urls")),
    path("profile/", include("tasty_recipes_app.profiles.urls"))
]
