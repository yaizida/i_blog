from django.contrib import admin

from .models import Post, Category, Location
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass