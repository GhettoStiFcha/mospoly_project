from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from mysite.models import Profile


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() and form.data['role']:
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            Profile(user=user, role=form.data['role']).save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
