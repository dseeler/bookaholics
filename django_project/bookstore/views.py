from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book
from .forms import RegistrationForm

def home(request):
    context = {
        'title': 'Home',
        'books': Book.objects.all(),
    }
    return render(request, 'bookstore/home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('bookstore-confirm_registration')
    else:
        form = RegistrationForm()

    return render(request, 'bookstore/register.html', {'form': form})

def confirm_registration(request):
    context = {
        'title': 'Confirmation',
    }
    return render(request, 'bookstore/confirm_registration.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('bookstore-home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('bookstore-home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {
            'title': 'Login',
        }
        return render(request, 'bookstore/signin.html', context)

def signout(request):
    logout(request)
    return redirect('bookstore-signin')

def book_detail(request, id):
    context = {
        'title': Book.objects.get(id=id).title,
        'book': Book.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/book_detail.html', context)

def edit_profile(request):
    context = {
        'title': 'Edit Profile',
    }
    return render(request,'bookstore/edit_profile.html',context)

def search(request):
    context = {
        'title': 'Explore',
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
    return render(request,'bookstore/cart.html',context)