from django.shortcuts import render
from .models import Book

def home(request):
    data = {
        'title': 'Home',
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/home.html', data)