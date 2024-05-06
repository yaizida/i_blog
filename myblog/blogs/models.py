from django.db import models

from user.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        'Зоголовок поста',
        max_length=254,
        blank=False,
        )
    text = models.TextField(
        'Текст поста',
        blank=False,
    )
    pub_date = models.DateField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=False,
    )
    is_published = models.BooleanField(
        blank=False,
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False
        )
    description = models.TextField(blank=False)
    slug = models.SlugField(
        unique=True,
        blank=False
    )
    is_published = models.BooleanField(default=True,)
    created_at = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False

    )
    is_published = models.BooleanField(
        default=True,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
