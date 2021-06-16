from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def my_texts(request):
    texts = request.user.texts.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(texts, 5)

    return render(request, 'pages/my_texts.html', context={
        'texts': paginator.get_page(page),
    })
