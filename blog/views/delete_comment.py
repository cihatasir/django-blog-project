from django.contrib.auth.decorators import login_required
from blog.models import TextModel, CommentModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required(login_url='/')
def delete_comment(request, id):
    comment = get_object_or_404(CommentModel, id=id)
    if comment.comment_author == request.user or comment.text.author == request.user:
        comment.delete()
        messages.success(request, 'Comment was deleted successfully.')
        return redirect('detail', slug=comment.text.slug)

    return redirect('base')


