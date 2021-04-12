from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, User, Promotion
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        ('Account', {'fields': ('email', 'password', 'first_name', 'last_name', 'phone')}),
        ('Address', {'fields': ('street', 'city', 'state', 'zip_code')}),
        ('Payment', {'fields': ('card_num', 'card_exp', 'card_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Promotions', {'fields': ('is_subscribed',)}),
        ('Status', {'fields': ('is_suspended',)})
    )

    add_fieldsets = (
        ('Account', {'fields': ('email', 'password', 'first_name', 'last_name', 'phone')}),
        ('Address', {'fields': ('street', 'city', 'state', 'zip_code')}),
        ('Payment', {'fields': ('card_num', 'card_exp', 'card_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Promotions', {'fields': ('is_subscribed',)}),
        ('Status', {'fields': ('is_suspended',)})
    )

    ordering = ('email',)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "year", "rating", "price")

class PromotionAdmin(admin.ModelAdmin):
    list_display = ("code", "percentage", "start_date", "end_date")

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(User, UserAdminConfig)
admin.site.register(Book, BookAdmin)
admin.site.register(Promotion, PromotionAdmin)
