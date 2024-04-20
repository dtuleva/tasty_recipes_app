from django.shortcuts import render, redirect

from tasty_recipes_app.auth_helper import get_profile
from tasty_recipes_app.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from tasty_recipes_app.recipes.models import Recipe


def profile_create(request):
    # Prevent creation of second profile
    if get_profile() is not None:
        return redirect("index")

    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "form": form,
        "no_profile": True
    }

    return render(request, "profile/create-profile.html", context)


def profile_details(request):
    profile = get_profile()
    recipes_count = Recipe.objects.count()
    context = {
        "profile": profile,
        "recipes_count": recipes_count,
    }
    return render(request, "profile/details-profile.html", context)


def profile_edit(request):
    profile = get_profile()
    if profile is None:
        return redirect("index")

    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    context = {
        "form": form,
    }
    return render(request, "profile/edit-profile.html", context)


def profile_delete(request):
    profile = get_profile()
    if profile is None:
        return redirect("index")

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        "form": form,
    }
    return render(request, "profile/delete-profile.html", context)
