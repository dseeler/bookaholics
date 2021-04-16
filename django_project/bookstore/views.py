from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.db.models import Sum

def home(request):
    print(getCartCount(request))
    context = {
        'title': 'Home',
        'books': Book.objects.all(),
        'cartCount': getCartCount(request),
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

            cart = Cart.objects.create_cart(user)

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
                if user.is_suspended:
                    return render(request, 'bookstore/suspended.html')
                else:
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
        'books': Book.objects.all(),
        'cartCount': getCartCount(request),
    }
    return render(request, 'bookstore/book_detail.html', context)

@login_required
def edit_profile(request):
    context = {
        'title': 'Edit Profile',
        'cartCount': getCartCount(request),
    }
    return render(request, 'bookstore/edit_profile.html', context)

@login_required
def edit_name(request):
    if request.method == "POST":
        user = request.user
        form = EditNameForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Name change successful!")

            # Send email notifying user of the change
            send_mail(
                'Bookstore account information changed',
                'Your Bookstore account information has been changed.',
                'csci4050.bookstore.app@gmail.com',
                [request.user.email],
                fail_silently=False,
            )

        else:
            messages.error(request, "Invalid name")
    return redirect('bookstore-edit_profile')


@login_required
def password_change_complete(request):
     # Send email notifying user of the change
    send_mail(
        'Bookstore account information changed',
        'Your Bookstore account information has been changed.',
        'csci4050.bookstore.app@gmail.com',
        [request.user.email],
        fail_silently=False,
    )

    messages.success(request, "Password change successful")
    return redirect('bookstore-edit_profile')


@login_required
def edit_phone(request):
    if request.method == "POST":
        user = request.user
        form = EditPhoneForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Phone change successful")

            # Send email notifying user of the change
            send_mail(
                'Bookstore account information changed',
                'Your Bookstore account information has been changed.',
                'csci4050.bookstore.app@gmail.com',
                [request.user.email],
                fail_silently=False,
            )

        else:
            messages.error(request, "Invalid phone number")
    return redirect('bookstore-edit_profile')


@login_required
def edit_address(request):
    if request.method == "POST":
        user = request.user
        form = EditAddressForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Address change successful")

            # Send email notifying user of the change
            send_mail(
                'Bookstore account information changed',
                'Your Bookstore account information has been changed.',
                'csci4050.bookstore.app@gmail.com',
                [request.user.email],
                fail_silently=False,
            )

        else:
            messages.error(request, "Invalid address")
    return redirect('bookstore-edit_profile')


@login_required
def edit_card(request):
    if request.method == "POST":
        user = request.user
        form = EditCardForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Credit card change successful")

            # Send email notifying user of the change
            send_mail(
                'Bookstore account information changed',
                'Your Bookstore account information has been changed.',
                'csci4050.bookstore.app@gmail.com',
                [request.user.email],
                fail_silently=False,
            )

        else:
            messages.error = (request, "Invalid credit card")
    return redirect('bookstore-edit_profile')


@login_required
def edit_subscribe(request):
    if request.method == "POST":
        user = request.user
        form = EditSubscribeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if request.POST['is_subscribed'] == "True":
                messages.success(request, "You are now subscribed to our promotions list!")
            elif request.POST['is_subscribed'] == "False":
                messages.success(request, "You have unsubscribed from our promotions list")

            # Send email notifying user of the change
            send_mail(
                'Bookstore account information changed',
                'Your Bookstore account information has been changed.',
                'csci4050.bookstore.app@gmail.com',
                [request.user.email],
                fail_silently=False,
            )

        else:
            messages.error(request, "Invalid input")
    return redirect('bookstore-edit_profile')

def password_reset_complete(request):
    messages.success(request, "Password change successful")
    return redirect('bookstore-signin')

def search(request):
    context = {
        'title': 'Explore',
        'books': Book.objects.all(),
        'cartCount': getCartCount(request),
    }
    return render(request,'bookstore/search.html',context)

def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart_id = Cart.objects.get(user=request.user.id)
            book = Book.objects.get(id=request.POST.get('book-id'))
            quantity = request.POST.get('quantity')

            # Update the quantity if the item is already in the cart
            if (CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id), book=book)):
                newQuantity = CartItem.objects.get(cart=Cart.objects.get(user=request.user.id), book=book).quantity + int(quantity)
                CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id), book=book).update(quantity=newQuantity)
            else:
                cart_item = CartItem.objects.add_cart_item(cart_id, book, quantity)

            messages.success(request, "{} ({}) added to cart".format(book.title, quantity))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            messages.info(request, "Sign in to add books to your cart")
            return redirect('bookstore-signin')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def checkout(request):
    context = {
        'title' : 'Checkout',
        'cartCount': getCartCount(request),
    }
    return render(request,'bookstore/checkout.html',context)

def order_history(request):
    context = {
        'title' : 'Order History',
        'cartCount': getCartCount(request),
    }
    return render(request,'bookstore/order_history.html',context)

def order_summary(request):
    context = {
        'title': 'Review Order Summary',
        'cartCount': getCartCount(request),
    }
    return render(request,'bookstore/order_summary.html',context)

def shopping_cart(request):
    cart = CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id))

    items = {}
    subtotal = 0

    for item in cart:
        total = item.book.price * item.quantity
        items[item] = {
            'book': item.book,
            'quantity': item.quantity,
            'total': total,
        }
        subtotal += total

    context = {
        'title': 'Shopping Cart',
        'cartCount': getCartCount(request),
        'cart': items,
        'subtotal': subtotal,
    }
    return render(request,'bookstore/cart.html',context)

def getCartCount(request):
    if request.user.is_authenticated:
        return CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id)).aggregate(Sum('quantity'))['quantity__sum']
    else:
        return ''