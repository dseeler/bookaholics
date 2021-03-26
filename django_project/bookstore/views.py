from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book, User
from .forms import RegistrationForm
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

def home(request):
    context = {
        'title': 'Home',
        'books': Book.objects.all(),
    }
    return render(request, 'bookstore/home.html', context)

def register(request):
    context = {
        'title': 'Sign Up',
    }

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Bookstore account'
            message = render_to_string('bookstore/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            context['email'] = to_email
            return render(request, 'bookstore/confirm_registration.html', context)
    else:
        form = RegistrationForm()

    return render(request, 'bookstore/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account verification successful! You can now login into your account.')
    else:
        messages.error(request, 'Account link is invalid!')
    return redirect('bookstore-signin')

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