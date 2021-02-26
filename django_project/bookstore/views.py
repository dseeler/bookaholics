from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from .forms import RegistrationForm

def home(request):
    context = {
        'title': 'Home',
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            return redirect('bookstore-confirm_registration')
    else:
        form = RegistrationForm()
    return render(request, 'bookstore/register.html', {'form': form})

def confirm_registration(request):
    context = {
        'title' : 'Confirm Registration',
    }
    return render(request,'bookstore/confirm_registration.html',context)

def login(request):
    context = {
        'title' : 'Login',
    }
    return render(request,'bookstore/login.html',context)

def edit_profile(request):
    context = {
        'title': 'Edit Profile',
    }
    return render(request,'bookstore/edit_profile.html',context)

def search(request):
    context = {
        'title': 'Search for Books',
        'books': Book.objects.all()
    }
    return render(request,'bookstore/search.html',context)

def checkout(request):
    context = {
        'title' : 'Checkout',
    }
    return render(request,'bookstore/checkout.html',context)

def order_history(request):
    context = {
        'title' : 'Order History',
    }
    return render(request,'bookstore/order_history.html',context)

def order_summary(request):
    context = {
        'title': 'Review Order Summary'
    }
    return render(request,'bookstore/order_summary.html',context)

def shopping_cart(request):
    context = {
        'title': 'Shopping Cart',
        'books': Book.objects.all()
    }
    return render(request,'bookstore/shopping_cart.html',context)