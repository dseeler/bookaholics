from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.forms import ModelForm

username_validator = UnicodeUsernameValidator()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=60, 
                            help_text='Required - add help text',
                            widget=(forms.TextInput(attrs={'class': 'form-control'})))

    first_name = forms.CharField(label='First Name', max_length=255,
                            help_text='Required - add help text',
                            widget=(forms.TextInput(attrs={'class': 'form-control'})))

    last_name = forms.CharField(label='Last Name', max_length=255,
                            help_text='Required - add help text',
                            widget=(forms.TextInput(attrs={'class': 'form-control'})))

    password1 = forms.CharField(label='Password',
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text="Required - add help text")

    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text='Required - add help text')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class EditNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class EditPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

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