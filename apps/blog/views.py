from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def home(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts,
        'primeiro': posts.first(),

    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    posts = models.Post.objects.get(pk=post_id)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_detail.html', context)