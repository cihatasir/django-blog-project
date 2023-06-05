from django.shortcuts import get_object_or_404, render
from blog.models import BlogModel, comment
from blog.forms import AddCommentModelForm

def detail(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug)
    comments = blog.blogsComments.all()
    
    if request.method == 'POST':
        add_comment_form = AddCommentModelForm(request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.comment_author = request.user
            comment.blog = blog
            comment.save()


    add_comment_form = AddCommentModelForm()


    return render(request, 'pages/detail.html', context={
        'blog': blog,
        'comments': comments,
        'add_comment_form': add_comment_form
    })