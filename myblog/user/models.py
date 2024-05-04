from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    sex = models.BooleanField(
        'Гендер',
        blank=True,
        null=True
        )
    nickname = models.CharField(
        'Никнейм',
        unique=True,
        max_length=20,
        blank=True,
        null=True
        )
    status = models.CharField(
        'Статус',
        max_length=30,
        blank=True,
        null=True
    )
    bio = models.TextField(
        'О себе',
        blank=True,
        null=True,
        )
