from enum import auto, unique
from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel


class TextModel(DateAbstractModel):
    image = models.ImageField(upload_to='texts_images')
    title = models.CharField(max_length=50)
    content = RichTextField()

    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='text')
    author = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='texts')

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        db_table = 'Text'

    def __str__(self):
        return self.title
