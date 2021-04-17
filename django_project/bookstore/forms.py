from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.forms import ModelForm
from django.core.validators import RegexValidator

username_validator = UnicodeUsernameValidator()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email',
                            help_text='Must be in proper email format and unique',
                            widget=(forms.TextInput(attrs={'class': 'form-control'})))

    first_name = forms.CharField(label='First Name', max_length=20,
                            help_text='Must be less than 20 characters ',
                            widget=(forms.TextInput(attrs={'class': 'form-control'})))

    last_name = forms.CharField(label='Last Name', max_length=20,
                            help_text='Must be less than 20 characters',
                            widget=(forms.TextInput(attrs={'class': 'form-control'})))

    password1 = forms.CharField(label='Password',
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text="Must contain letters and digits")

    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text='Must be the same as password')


    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_subscribed')
        labels = {"is_subscribed": "Subscribe to our promotions list? "}

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('id', 'user')


class EditNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class EditPhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone',)

class EditAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('street', 'city', 'state', 'zip_code')

class EditCardForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('card_num', 'card_exp', 'card_code')

class EditSubscribeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_subscribed',)