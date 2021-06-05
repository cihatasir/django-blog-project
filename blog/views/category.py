from django.core import paginator
from django.shortcuts import render, get_object_or_404
from blog.models import TextModel, CategoryModel
from django.core.paginator import Paginator

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug=categorySlug)
    texts = category.text.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(texts, 2)

    return render(request, 'pages/category.html', context={
        'texts': paginator.get_page(page),
        'category_title': category.name
    })
