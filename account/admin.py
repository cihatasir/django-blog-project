from account.models import CustomUserModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel


@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Change Area', {
            'fields': ['avatar']
        }),
    )
