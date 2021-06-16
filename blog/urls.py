from blog.views import detail, category, base, contact, my_texts, add_text, update_text, delete_text, delete_comment
from django.urls import path, include


urlpatterns = [
    path('', base, name='anasayfa'),
    path('contact', contact, name='iletisim'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my_texts', my_texts, name='my_texts'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-text', add_text, name='add-text'),
    path('update-text/<slug:slug>', update_text, name='update-text'),
    path('delete-text/<slug:slug>', delete_text, name='delete-text'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),
]
