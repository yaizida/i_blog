from django.db import models


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
        'user.User',
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
    pass


class Location(models.Model):
    pass
