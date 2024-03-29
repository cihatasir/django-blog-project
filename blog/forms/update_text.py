from django import forms
from blog.models import BlogModel


class UpdateTextFormModel(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude = ('author', 'slug')

        