from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # `required=True` is the default

    class Meta:  # its about cofigurations for example now we are saying that its a "User model" and it has these fields.
        model = User
        fields = ['username', 'email', 'password1', 'password2']