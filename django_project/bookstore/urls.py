from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('home', views.home, name='bookstore-home'),
    path('register', views.register, name='bookstore-register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('confirm_registration', views.confirm_registration, name='bookstore-confirm_registration'),
    path('signin', views.signin, name='bookstore-signin'),
    path('signout', views.signout, name='bookstore-signout'),
    path('edit_profile', views.edit_profile, name='bookstore-edit_profile'),
    path('edit_name', views.edit_name, name="bookstore-edit_name"),
    path('edit_phone', views.edit_phone, name="bookstore-edit_phone"),
    path('edit_address', views.edit_address, name="bookstore-edit_address"),
    path('edit_card', views.edit_card, name="bookstore-edit_card"),
    path('edit_subscribe', views.edit_subscribe, name="bookstore-edit_subscribe"),
    path('search', views.search, name='bookstore-search'),
    path('book_detail/<str:title>/', views.book_detail, name='bookstore-book_detail'),
    path('add_to_cart', views.add_to_cart, name='bookstore-add_to_cart'),
    path('checkout', views.checkout, name='bookstore-checkout'),
    path('order_history', views.order_history, name='bookstore-order_history'),
    path('order_summary', views.order_summary, name='bookstore-order_summary'),
    path('shopping_cart', views.shopping_cart, name='bookstore-shopping_cart'),
    path('change_quantity', views.change_quantity, name='bookstore-change_quantity'),
    path('redeem_promo', views.redeem_promo, name='bookstore-redeem_promo'),
    path('place_order', views.place_order, name=('bookstore-place_order')),
    path('reorder_book', views.reorder_book, name='bookstore-reorder_book'),
    path('reorder_all', views.reorder_all, name='bookstore-reorder_all'),
    path('filter_search', views.filter_search, name='bookstore-filter_search'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='bookstore/password-reset/password_reset.html',
             subject_template_name='bookstore/password-reset/password_reset_subject.txt',
             email_template_name='bookstore/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='bookstore/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='bookstore/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete, name="password_reset_complete"),
    path(
        'change-password',
        auth_views.PasswordChangeView.as_view(
            template_name='bookstore/change_password.html',
            success_url='password-change-complete'
        ),
        name='change-password'
    ),
    path('password-change-complete', views.password_change_complete, name="pasword_change_complete")
]
