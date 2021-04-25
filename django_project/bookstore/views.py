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
from django.http import JsonResponse
from datetime import date, datetime
import json


def home(request):
    context = {
        'title': 'Home',
        'best_sellers': Book.objects.filter(rating=5).order_by('?'),
        'new_arrivals': Book.objects.all(),
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
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
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
        messages.success(
            request, 'Account verification successful! You can now login into your account.')
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


def book_detail(request, title):
    book = Book.objects.get(title=title)
    context = {
        'title': book.title,
        'book': book,
        'other_books': Book.objects.filter(genre=book.genre).order_by('?'),
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
                messages.success(
                    request, "You are now subscribed to our promotions list!")
            elif request.POST['is_subscribed'] == "False":
                messages.success(
                    request, "You have unsubscribed from our promotions list")

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
    try:
        # If accessing search page without providing query
        books = Book.objects.all().order_by('title')
        header = 'Select books to add to your cart'

        # If query is provided (or clicking a genre link on Home page)
        if request.method == 'GET':
            category = request.GET.get('category')
            input = request.GET.get('input')

            if category is not None:
                # If query is requested from the Search page (filtered)
                genre = request.GET.get('genre')
                price_range = request.GET.get('price-range')
                rating = request.GET.get('rating')

                if category == 'Title':
                    books = Book.objects.filter(title__contains=input)
                elif category == 'Genre':
                    books = Book.objects.filter(genre__contains=input)
                elif category == 'Author':
                    books = Book.objects.filter(author__contains=input)
                elif category == 'ISBN':
                    books = Book.objects.filter(isbn=input)
                elif category == 'Year':
                    books = Book.objects.filter(year=input)

                # Filter genre
                if genre is not None:            
                    books = books.filter(genre=genre)
                    
                # Filter rating
                if rating is not None:
                    books = books.filter(rating=rating)

                # Filter price
                if price_range is not None:
                    if price_range == '<10':
                        books = books.filter(price__lt=10)
                    elif price_range == '10-20':
                        books = books.filter(price__gte=10, price__lt=20)
                    elif price_range == '20>':
                        books = books.filter(price__gte=20)
                
                # Sort books alphabetically
                books = books.order_by('title')

                header = str(len(books)) + " results found for '" + input + "'"

        context = {
            'title': 'Explore',
            'header': header,
            'books': books,
            'cartCount': getCartCount(request),
        }
        return render(request, 'bookstore/search.html', context)

    except:
        return redirect('bookstore-search')

@login_required
def add_to_cart(request):
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:

                cart_id = Cart.objects.get(user=request.user.id)
                book = Book.objects.get(id=request.POST.get('book-id'))
                quantity = request.POST.get('quantity')
                # Update the quantity if the item is already in the cart
                if (CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id), book=book)):
                    newQuantity = CartItem.objects.get(cart=Cart.objects.get(
                        user=request.user.id), book=book).quantity + int(quantity)
                    CartItem.objects.filter(cart=Cart.objects.get(
                        user=request.user.id), book=book).update(quantity=newQuantity)
                else:
                    cart_item = CartItem.objects.add_cart_item(
                        cart_id, book, quantity)

                messages.success(
                    request, "{} ({}) added to cart".format(book.title, quantity))
                    
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                messages.info(request, "Sign in to add books to your cart")
                return redirect('bookstore-signin')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        messages.info(request, "Something went wrong")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def checkout(request):
    cart = CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id))

    items = {}
    subtotal = 0

    for item in cart:
        total = item.book.price * item.quantity
        items[item] = {
            'book': item.book,
            'quantity': item.quantity,
            'total': total,
            'cart': item.cart
        }
        subtotal += total

    # Redirect to Home if cart is empty
    if not bool(items):
        messages.info(request, "You can't checkout with an empty cart")
        return redirect('bookstore-home')

    context = {
        'title': 'Shopping Cart',
        'cartCount': getCartCount(request),
        'cart': items,
        'subtotal': subtotal,
    }
    return render(request, 'bookstore/checkout.html', context)

@login_required
def order_history(request):
    order_data = {}
    orders = Order.objects.filter(user=request.user)

    index = 0
    for order in orders:
        order_items = OrderItem.objects.filter(order=order)
        order_data[index] = {
            'order': order,
            'items': order_items
        }
        index += 1

    context = {
        'title': 'Order History',
        'cartCount': getCartCount(request),
        'order_data': order_data,
    }
    return render(request, 'bookstore/order_history.html', context)


def order_summary(request):
    context = {
        'title': 'Review Order Summary',
        'cartCount': getCartCount(request),
    }
    return render(request, 'bookstore/order_summary.html', context)

@login_required
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
            'cart': item.cart
        }
        subtotal += total

    context = {
        'title': 'Shopping Cart',
        'cartCount': getCartCount(request),
        'cart': items,
        'subtotal': subtotal,
    }
    return render(request, 'bookstore/cart.html', context)

# Ajax quantity update request
@login_required
def change_quantity(request):
    try:
        if request.method == 'POST' and request.is_ajax():
            book = request.POST.get('book_id')
            cart = request.POST.get('cart_id')
            quantity = request.POST.get('quantity')

            # Delete item and refresh page if quantity is changed to 0
            if int(quantity) == 0:
                CartItem.objects.filter(cart=cart, book=book).delete()
                return JsonResponse(["refresh"], safe=False)
            else:
                CartItem.objects.filter(
                    cart=cart, book=book).update(quantity=quantity)

            # Send JsonResponse with updated data
            data = [{'book': book, 'quantity': quantity,
                     'cartCount': getCartCount(request)}]
            return JsonResponse(data, safe=False)
    except:
        messages.info(request, "Something went wrong")
        return redirect('bookstore-shopping_cart')

# Ajax search filtering
def filter_search(request):
    try:
        if request.method == 'POST' and request.is_ajax():
            genre = request.POST.get('genre')
            price_range = request.POST.get('price_range')
            rating = request.POST.get('rating')

            books = Book.objects.all()

            # Filter genre
            if genre is not None:
                genre = genre.replace("\"", "")
                if genre != "Any":
                    books = books.filter(genre=genre)

            # Filter price
            if price_range is not None:
                price_range = price_range.replace("\"", "")
                if price_range == '<10':
                    books = books.filter(price__lt=10)
                elif price_range == '10-20':
                    books = books.filter(price__gte=10, price__lt=20)
                elif price_range == '20>':
                    books = books.filter(price__gte=20)

            # Filter rating
            if rating is not None:
                rating = rating.replace("\"", "")
                if rating != "Any":
                    books = books.filter(rating=rating)

            # Send JsonResponse with filtered books
            json_books = {}
            for book in books:
                json_books[book.id] = {
                    'title': book.title,
                    'author': book.author,
                    'image': book.image,
                    'price': book.price,
                    'rating': book.rating
                }

            data = [json_books]
            return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)
        messages.info(request, "Something went wrong")
        return redirect('bookstore-shopping_cart')

@login_required
def redeem_promo(request):
    try:
        if request.method == 'POST' and request.is_ajax():
            code = request.POST.get('promo_code').replace("\"", "")
            
            promotion = Promotion.objects.filter(code=code)            

            today = date.today()     
 
            if len(promotion) == 0:
                return JsonResponse(['Invalid code'], safe=False)
            else:
                if today > promotion[0].end_date:
                    return JsonResponse(['This code expired on {}'.format(promotion[0].end_date)], safe=False) 
                elif today < promotion[0].start_date:
                    print('hi')
                    return JsonResponse(['This promotion starts on {}'.format(promotion[0].start_date)], safe=False)
                else:
                    return JsonResponse([promotion[0].percentage], safe=False)
    
    except:
        return redirect('bookstore-checkout')

@login_required
def place_order(request):
    if request.method == 'POST':
        user = request.user
        total = request.POST.get('total-input')
        promo_code = request.POST.get('promo-input')
        today = date.today()
        time = datetime.now().strftime("%H:%M:%S")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        card_name = request.POST.get('card_name')
        card_num = request.POST.get('card_num')
        card_exp = request.POST.get('card_exp')
        card_code = request.POST.get('card_code')

        order = Order.objects.create_order(user, total, today, time, first_name, last_name, street, city, state, zip_code, card_name, card_num, card_exp, card_code)

        # Add promotion if one was applied
        if promo_code != '':
            promotion = Promotion.objects.get(code=promo_code)
            order.promotion = promotion
            order.save()
    

       # Add items to OrderItems
        cart_items = CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id))
        for item in cart_items:        
            order_item = OrderItem.objects.add_order_item(order, item.book, item.quantity)

        email_body = "Order ID: " + str(order.id)
        email_body += "\nOrder date and time: " + str(order.date) + " at " + str(order.time)
        email_body += "\nOrdered by: " + str(order.first_name) + " " + str(order.last_name)
        email_body += "\n\nShipping information:\n" + str(order.street)
        email_body += "\n" + str(order.city) + ", " + str(order.state) + " " + str(order.zip_code)
        email_body += "\n\nOrdered items: "

        # Add items to email body and clear cart
        for item in cart_items:
            email_body += "\n" + str(item.book.title) + " (" + str(item.quantity) + "): $" + str(item.book.price) 
            item.delete()

        email_body += "\n\nTotal: $" + str(order.total)    

        # Send order confirmation email
        send_mail(
            'Your order has been placed!',
            email_body,
            'csci4050.bookstore.app@gmail.com',
            [request.user.email],
            fail_silently=False,
        )

        # TO-DO:
        # Add address2?
        # Order status?

        messages.success(request, "Your order has been placed! Confirmation code: {}".format(order.id))
        return redirect('bookstore-home')

@login_required
def reorder_book(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST.get('book-id'))

        # Find the User's cart and remove any existing items
        cart = cart=Cart.objects.get(user=request.user.id)
        CartItem.objects.filter(cart=cart).delete()

        # Add the book to the cart
        cart_item = CartItem.objects.add_cart_item(cart, book, 1)

        messages.success(request, "{} (1) added to cart".format(book.title))
        return redirect('bookstore-checkout')

@login_required
def reorder_all(request):
    if request.method == 'POST':
        order = request.POST.get('order')

        # Find the books using the extracted order ID
        order_items = OrderItem.objects.filter(order=order)

        # Find the User's cart and remove any existing items
        cart = cart=Cart.objects.get(user=request.user.id)
        CartItem.objects.filter(cart=cart).delete()

        # Add the books from the order to the cart
        for item in order_items:
            cart_item = CartItem.objects.add_cart_item(cart, item.book, item.quantity)

        messages.success(request, "Books added to cart")
        return redirect('bookstore-checkout')


def getCartCount(request):
    if request.user.is_authenticated:
        return CartItem.objects.filter(cart=Cart.objects.get(user=request.user.id)).aggregate(Sum('quantity'))['quantity__sum']
    else:
        return ''
