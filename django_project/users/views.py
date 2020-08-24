from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
  # we have these messages:
    # messages.debug
    # messages.info
    # messages.success
    # messages.warning
    # messages.error
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # it will automaticly hash passwords
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Accont created for {username}!')
            # return redirect('blog-home')
            messages.success(request, f'Hi {username}!  Your accont created and now you can login')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')