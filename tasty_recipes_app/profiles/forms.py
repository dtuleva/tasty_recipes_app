from django import forms

from tasty_recipes_app.profiles.models import Profile
from tasty_recipes_app.recipes.models import Recipe


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ("bio",)


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Recipe.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
