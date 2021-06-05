from django.db.models import fields
from blog.models.contact import ContactModel
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name_surname', 'email', 'message')
 