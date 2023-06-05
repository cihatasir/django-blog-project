from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def my_blogs(request):
    blogs = request.user.blogs.order_by('-id')

    return render(request, 'pages/my_blogs.html', context={
        'blogs': blogs
    })

