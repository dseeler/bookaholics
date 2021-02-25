from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='bookstore-home'),
    path('register', views.register, name='bookstore-register'),
    path('confirm_registration',views.confirm_registration,name='bookstore-confirm_registration'),
    path('login',views.login,name='bookstore-login'),
    path('edit_profile',views.edit_profile, name='bookstore-edit_profile'),
    path('search',views.search, name='bookstore-search'),
    path('checkout',views.checkout,name='bookstore-checkout'),
    path('order_history',views.order_history,name='bookstore-order_history'),
    path('order_summary',views.order_summary,name='bookstore-order_summary'),
    path('shopping_cart',views.shopping_cart,name='bookstore-shopping_cart'),
]
