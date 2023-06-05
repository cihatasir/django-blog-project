from django.shortcuts import render
from blog.models import BlogModel
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models.category import CategoryModel

def base(request):
    sorgu = request.GET.get('sorgu')
    blogs = BlogModel.objects.order_by('-id')

    if sorgu:
        blogs = blogs.filter(
            Q(title__icontains=sorgu) |
            Q(content__icontains=sorgu)
        ).distinct()

    page = request.GET.get('page')
    paginator = Paginator(blogs, 2)

    return render(request, 'pages/main.html', context={
        'blogs': paginator.get_page(page)
    })
