import mimetypes

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from mysite.forms import MusicForm
from mysite.models import Profile, Music


def index(request):
    items = Music.objects.all()
    return render(request, "index.html", {'music': items})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() and form.data['role']:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username, password=password)
            authenticate(user)
            Profile(user=user, role=form.data['role']).save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Music(title=request.POST['title'], file=request.FILES['file'], image=request.FILES['image'],
                           user=request.user)
            newdoc.save()
            return redirect('index')
    else:
        form = MusicForm()

    return render(request, 'upload.html', {'form': form})


def audio(request, music_id):
    item = Music.objects.get(pk=music_id)
    return render(request, 'audio.html', {'music': item})


def upload(request):
    return render(request, 'upload.html')
