from blog.views.category import category
from blog.views.base import base
from django.urls import path, include
from blog.views import contact, base, my_texts

urlpatterns = [
    path('', base, name='anasayfa'),
    path('contact', contact, name='iletisim'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my_texts', my_texts, name='my_texts'),
]
