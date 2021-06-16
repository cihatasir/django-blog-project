from django import forms
from blog.models import TextModel


class UpdateTextFormModel(forms.ModelForm):
    class Meta:
        model = TextModel
        exclude = ('author', 'slug')

        