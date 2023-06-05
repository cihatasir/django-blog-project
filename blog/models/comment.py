from django.db import models
from django.contrib.auth.models import User
from blog.models import BlogModel
from blog.abstract_models import DateAbstractModel


class CommentModel(DateAbstractModel):
    comment_author = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')

    blog = models.ForeignKey(
        BlogModel, on_delete=models.CASCADE, related_name='blogsComments')

    comment = models.TextField()

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment_author.username
