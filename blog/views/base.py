from django.shortcuts import render
from blog.models import TextModel
from django.core.paginator import Paginator
from django.db.models import Q

def base(request):
    sorgu = request.GET.get('sorgu')
    texts = TextModel.objects.order_by('-id')

    if sorgu:
        texts = texts.filter(
            Q(title__icontains=sorgu) |
            Q(content__icontains=sorgu)
        ).distinct()

    page = request.GET.get('page')
    paginator = Paginator(texts, 2)

    return render(request, 'pages/anasayfa.html', context={
        'texts': paginator.get_page(page)
    })
