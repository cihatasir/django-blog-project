from django.contrib.auth.decorators import login_required
from blog.models import BlogModel
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='/')
def delete_blog(request, slug):
    get_object_or_404(BlogModel, slug=slug, author=request.user).delete()
    return redirect('my_blogs')


