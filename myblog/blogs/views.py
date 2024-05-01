from django.shortcuts import render
from django.views import View

from .test_utils import POSTS


def index(request):
    context = {'posts': POSTS}
    return render(request, 'blogs/index.html', context)


def post_detail(request):
    pass


def category_posts(request):
    pass
