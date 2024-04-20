from django.urls import path

from tasty_recipes_app.core.views import index

urlpatterns = (
    path("", index, name="index"),
)
