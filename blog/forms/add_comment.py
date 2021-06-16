from django import forms
from django.forms import fields
from blog.models import CommentModel

class AddCommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', )