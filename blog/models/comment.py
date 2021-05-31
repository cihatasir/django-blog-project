from django.db import models
from django.contrib.auth.models import User
from blog.models import TextModel
from blog.abstract_models import DateAbstractModel


class CommentModel(DateAbstractModel):
    comment_author = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')

    text = models.ForeignKey(
        TextModel, on_delete=models.CASCADE, related_name='textsComments')

    comment = models.TextField()

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment_author.username
