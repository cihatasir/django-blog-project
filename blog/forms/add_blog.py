from django import forms
from blog.models import BlogModel

class AddBlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude = ('author', 'slug')

        