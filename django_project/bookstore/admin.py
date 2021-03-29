from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, User
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        ('Account', {'fields': ('email', 'password', 'first_name', 'last_name', 'phone')}),
        ('Address', {'fields': ('street', 'city', 'state', 'zip_code')}),
        ('Payment', {'fields': ('card_num', 'card_exp', 'card_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    add_fieldsets = (
        ('Account', {'fields': ('email', 'password', 'first_name', 'last_name', 'phone')}),
        ('Address', {'fields': ('street', 'city', 'state', 'zip_code')}),
        ('Payment', {'fields': ('card_num', 'card_exp', 'card_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    ordering = ('email',)

admin.site.register(User, UserAdminConfig)
admin.site.register(Book)