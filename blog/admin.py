from django.contrib import admin
from blog.models import(CommentModel, TextModel,
                        CategoryModel
                        )


admin.site.register(CategoryModel)


class TextsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'date_created', 'date_edit'
    )


admin.site.register(TextModel, TextsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'date_created', 'date_edited')
    search_fields = ('comment_author__User',)


admin.site.register(CommentModel, CommentAdmin)
