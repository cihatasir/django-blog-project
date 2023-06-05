from django.core import paginator
from django.shortcuts import render, get_object_or_404
from blog.models import BlogModel, CategoryModel
from django.core.paginator import Paginator

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug=categorySlug)
    blogs = category.blog.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(blogs, 2)

    return render(request, 'pages/category.html', context={
        'blogs': paginator.get_page(page),
        'category_title': category.name
    })
