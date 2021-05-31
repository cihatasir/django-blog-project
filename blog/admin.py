from blog.models.contact import ContactModel
from django.contrib import admin
from blog.models import(CommentModel, TextModel,
                        CategoryModel, ContactModel
                        )


admin.site.register(CategoryModel)


@admin.register(TextModel)
class TextsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'date_created', 'date_edited'
    )


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'date_created', 'date_edited')
    search_fields = ('comment_author__User',)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created')
    search_fields = ('email__User',)
