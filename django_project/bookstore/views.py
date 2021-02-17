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
            return redirect('bookstore-home')
    else:
        form = RegistrationForm()
    return render(request, 'bookstore/register.html', {'form': form})