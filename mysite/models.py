from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Role(models.IntegerChoices):
        MUSICIAN = 0
        GAMEDEV = 1

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=Role.choices, default=Role.MUSICIAN)

