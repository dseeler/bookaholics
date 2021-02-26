from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username*", max_length=20)
    password = forms.CharField(label="Password*", max_length=20,  widget=forms.PasswordInput)
    email = forms.EmailField(label="Email*")
    phone = forms.CharField(label="Phone*", max_length=10)
    card_num = forms.CharField(label="Card number*", max_length=16)
    card_exp = forms.CharField(label="Expiration date*", max_length=5)
    card_code = forms.CharField(label="Security code*", max_length=3)

    class Meta:
        model = User
        fields = ("username", "password", "email", "phone", "card_num", "card_exp", "card_code")
