from django import forms

from tasty_recipes_app.recipes.models import Recipe


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(),
            "cuisine_type": forms.Select(),
            "ingredients": forms.Textarea(attrs={"placeholder": "ingredient1, ingredient2, ..."}),
            "instructions": forms.Textarea(attrs={"placeholder": "Enter detailed instructions here..."}),
            "cooking_time": forms.NumberInput(),
            "image_url": forms.URLInput(attrs={"placeholder": "Optional image URL here..."}),
        }


class CreateRecipeForm(BaseRecipeForm):
    pass


class EditRecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(BaseRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field_name in self.fields.keys():
            self.fields[field_name].disabled = True
            self.fields[field_name].widget.attrs["readonly"] = True
