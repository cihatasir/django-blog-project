from django.db import models
from django.contrib.auth.models import User
from blog.models import TextModel


class CommentModel(models.Model):
    comment_author = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')

    text = models.ForeignKey(
        TextModel, on_delete=models.CASCADE, related_name='textsComments')

    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment_author.username
