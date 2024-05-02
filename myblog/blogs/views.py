from django.shortcuts import render

from .test_utils import POSTS


def index(request):
    context = {'posts': POSTS}
    return render(request, 'blogs/index.html', context)


def post_detail(request, pk):
    context = {'post': POSTS[pk]}
    return render(request, 'blogs/detail.html', context)


def category_posts(request, category_slug):
    context = {'slug': category_slug}
    return render(request, 'blogs/category.html', context)
