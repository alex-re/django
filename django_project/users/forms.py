from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import ReCaptchaField
from django.conf import settings


class UserRegisterForm(UserCreationForm, forms.Form):
    email = forms.EmailField(required=True)  # `required=True` is the default
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        required=True,
    )

    class Meta:  # its about cofigurations for example now we are saying that its a "User model" and it has these fields.
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']