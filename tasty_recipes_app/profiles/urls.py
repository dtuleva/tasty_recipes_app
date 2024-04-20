"""
http://localhost:8000/profile/create/ - Profile create page
http://localhost:8000/profile/details/ - Profile details page
http://localhost:8000/profile/edit/ - Profile edit page
http://localhost:8000/profile/delete/ - Profile delete page
"""
from django.urls import path

from tasty_recipes_app.profiles.views import profile_create, profile_details, profile_edit, profile_delete

urlpatterns = (
    path("create/", profile_create, name="profile_create"),
    path("details/", profile_details, name="profile_details"),
    path("edit/", profile_edit, name="profile_edit"),
    path("delete/", profile_delete, name="profile_delete"),
)