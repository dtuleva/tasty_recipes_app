from django.shortcuts import render

from tasty_recipes_app.auth_helper import no_profile_created


def index(request):
    no_profile = no_profile_created()
    context = {
        "no_profile": no_profile,
    }

    return render(request, "core/home-page.html", context)
