from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=10.00)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

class UserAccountManager(BaseUserManager):

    def create_user(self, email, password, first_name, last_name, phone, street, city, state, zip_code, card_num, card_exp, card_code, **other_feilds):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone, street=street, city=city, 
        state=state, zip_code=zip_code, card_num=card_num, card_exp=card_exp, card_code=card_code, **other_feilds)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, first_name, last_name, phone, street, city, state, zip_code, card_num, card_exp, card_code, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, first_name, last_name, phone, street, city, state, zip_code, card_num, card_exp, card_code, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    card_num = models.CharField(max_length=16, null=True, blank=True)
    card_exp = models.CharField(max_length=5, null=True, blank=True)
    card_code = models.CharField(max_length=3, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'street', 'city', 'state', 'zip_code', 'card_num', 'card_exp', 'card_code', 'is_staff', 'is_active']

    def __str__(self):
        return self.email