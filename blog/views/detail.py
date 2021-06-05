from django.shortcuts import get_object_or_404, render
from blog.models import TextModel, comment

def detail(request, slug):
    text = get_object_or_404(TextModel, slug=slug)
    comments = text.textsComments.all()

    return render(request, 'pages/detail.html', context={
        'text': text,
        'comments': comments
    })