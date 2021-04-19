from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
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
        ('Payment', {'fields': ('card_name', 'card_num', 'card_exp', 'card_code')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Promotions', {'fields': ('is_subscribed',)}),
        ('Status', {'fields': ('is_suspended',)})
    )

    ordering = ('email',)

    # Add custom js and css to User model in admin view
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'admin/js/user.js',
            )
        css = {'all': ('admin/css/user.css', )}  

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "year", "rating", "price")

class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")

    # Disable edit permissions for Promotion
    def has_change_permission(self, request, obj=None):
        return False

class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "book", "quantity")

class PromotionAdmin(admin.ModelAdmin):
    list_display = ("code", "percentage", "start_date", "end_date")

    # Disable delete permissions for Promotion
    def has_delete_permission(self, request, obj=None):
        return False
    
    # Disable edit permissions for Promotion
    def has_change_permission(self, request, obj=None):
        return False

    # Add custom js and css to Promotion model in admin view
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'admin/js/promotion.js',
            )
        css = {'all': ('admin/css/promotion.css', )}  

admin.site.register(User, UserAdminConfig)
admin.site.register(Book, BookAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Promotion, PromotionAdmin)
