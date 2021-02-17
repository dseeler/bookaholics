from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='bookstore-home'),
    path('register', views.register, name='bookstore-register'),
]