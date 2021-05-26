from blog.models.text import TextModel
from django.contrib import admin
from blog.models import CategoryModel

admin.site.register(CategoryModel)


class TextsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'date_created', 'date_edit'
    )


admin.site.register(TextModel, TextsAdmin)
