from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail
import datetime
from django_cryptography.fields import encrypt
import uuid

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=10.00)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=20, default="Fiction")
    rating = models.IntegerField(default=4)

    def __str__(self):
        return self.title

class Promotion(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    percentage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def clean(self):
        # Verify start date is before end date
        if self.start_date is not None and self.end_date is not None and self.end_date < self.start_date:
            raise ValidationError("End date should be greater than start date")

    def __str__(self):
        return self.code

# Called after a promotion is saved
@receiver(post_save, sender=Promotion)
def email_promotion(sender, instance, **kwargs):
    subject = "There's a new promotion at Baldwin Books!"
    message = instance.description + "\nUse code: " + instance.code + "\n\nOFFER EXPIRES " + instance.end_date.strftime("%Y-%m-%d")
    sender = 'csci4050.bookstore.app@gmail.com'
    recipients = []

    # Add users who are subscribed to promotions
    for user in User.objects.all():
        if user.is_subscribed:
            recipients.append(user.email) 

    messages = [(subject, message, sender, [recipient]) for recipient in recipients]

    # Send promo to all users (recipients are hidden)
    send_mass_mail(messages)


class UserAccountManager(BaseUserManager):

    def create_user(self, email, password, first_name, last_name, phone, street, city, state, zip_code, card_name, card_num, card_exp, card_code, is_subscribed, **other_feilds):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone, street=street, city=city, 
        state=state, zip_code=zip_code, card_name=card_name, card_num=card_num, card_exp=card_exp, card_code=card_code, is_subscribed=is_subscribed, **other_feilds)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, first_name, last_name, phone, street, city, state, zip_code, card_name, card_num, card_exp, card_code, is_subscribed, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, first_name, last_name, phone, street, city, state, zip_code, card_name, card_num, card_exp, card_code, is_subscribed, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    card_name = encrypt(models.CharField(max_length=255, null=True, blank=True))
    card_num = encrypt(models.CharField(max_length=16, null=True, blank=True))
    card_exp = encrypt(models.CharField(max_length=5, null=True, blank=True))
    card_code = encrypt(models.CharField(max_length=3, null=True, blank=True))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'street', 'city', 'state', 'zip_code', 'card_name', 'card_num', 'card_exp', 'card_code', 'is_staff', 'is_active', 'is_suspended', 'is_subscribed']

    def __str__(self):
        return self.email


class CartManager(models.Manager):
    def create_cart(self, user):
        cart = self.create(user=user)
        return cart


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

class CartItemManager(models.Manager):
    def add_cart_item(self, cart, book, quantity):
        cart_item = self.create(cart=cart, book=book, quantity=quantity)
        return cart_item

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    objects = CartItemManager()

    def __str__(self):
        return str(self.id)

class OrderManager(models.Manager):
    def create_order(self, user, total, date, time, first_name, last_name, street, city, state, zip_code, card_name, card_num, card_exp, card_code):
        order = self.create(user=user, total=total, date=date, time=time, first_name=first_name, last_name=last_name, street=street, city=city, 
        state=state, zip_code=zip_code, card_name=card_name, card_num=card_num, card_exp=card_exp, card_code=card_code)
        return order

class Order(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, max_length=10)
    status = models.CharField(max_length=255, default="Confirmed")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=5)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)
    card_name = encrypt(models.CharField(max_length=255))
    card_num = encrypt(models.CharField(max_length=16))
    card_exp = encrypt(models.CharField(max_length=5))
    card_code = encrypt(models.CharField(max_length=3))

    objects = OrderManager()

    def __str__(self):
        return str(self.id)
    
class OrderItemManager(models.Manager):
    def add_order_item(self, order, book, quantity):
        order_item = self.create(order=order, book=book, quantity=quantity)
        return order_item

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    objects = OrderItemManager()

    def __str__(self):
        return str(self.id)
