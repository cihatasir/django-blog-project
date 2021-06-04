from blog.views.base import base
from django.urls import path, include
from blog.views import contact, base

urlpatterns = [
    path('', base),
    path('contact', contact),
]
