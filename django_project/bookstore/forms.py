from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={'unique': "A user with that username already exists."},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(label='Password',
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())

    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text='Just Enter the same password, for confirmation')
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')