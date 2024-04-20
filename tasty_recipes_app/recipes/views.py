from django.shortcuts import render, redirect

from tasty_recipes_app.auth_helper import get_profile
from tasty_recipes_app.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from tasty_recipes_app.recipes.models import Recipe


def catalogue(request):
    if get_profile() is None:
        return redirect("index")

    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request, "recipe/catalogue.html", context)


def recipe_create(request):
    if get_profile() is None:
        return redirect("index")

    if request.method == "GET":
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "form": form,
    }
    return render(request, "recipe/create-recipe.html", context)


def recipe_details(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    context = {
        "recipe": recipe
    }
    return render(request, "recipe/details-recipe.html", context)


def recipe_edit(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "recipe/edit-recipe.html", context)


def recipe_delete(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "recipe/delete-recipe.html", context)
