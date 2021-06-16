from django.shortcuts import get_object_or_404, render
from blog.models import TextModel, comment
from blog.forms import AddCommentModelForm

def detail(request, slug):
    text = get_object_or_404(TextModel, slug=slug)
    comments = text.textsComments.all()
    
    if request.method == 'POST':
        add_comment_form = AddCommentModelForm(request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.text = text
            comment.save()


    add_comment_form = AddCommentModelForm()


    return render(request, 'pages/detail.html', context={
        'text': text,
        'comments': comments,
        'add_comment_form': add_comment_form
    })