from django import forms
from blog.models import TextModel


class AddTextModelForm(forms.ModelForm):
    class Meta:
        model = TextModel
        exclude = ('author', 'slug')

        