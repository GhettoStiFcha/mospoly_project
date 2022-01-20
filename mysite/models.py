from django.contrib.auth.models import User
from django.db import models

from mysite.utils import user_directory_path


class Profile(models.Model):
    class Role(models.IntegerChoices):
        MUSICIAN = 0
        GAMEDEV = 1

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=Role.choices, default=Role.MUSICIAN)


class Music(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=user_directory_path)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

