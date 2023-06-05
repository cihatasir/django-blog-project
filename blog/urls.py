from blog.views import detail, category, base, contact, my_blogs, add_blog, update_blog, delete_blog, delete_comment, blogs
from django.urls import path, include


urlpatterns = [
    path('', base, name='main'),
    path('contact', contact, name='iletisim'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my_blogs', my_blogs, name='my_blogs'),
    path('blogs', blogs, name='blogs'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-blog', add_blog, name='add-blog'),
    path('update-blog/<slug:slug>', update_blog, name='update-blog'),
    path('delete-blog/<slug:slug>', delete_blog, name='delete-blog'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),
]
