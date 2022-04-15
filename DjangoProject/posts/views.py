from django.shortcuts import render

from django.views.generic import ListView
from .models import Post

class PostsHomePage(ListView):
    model = Post
    template_name = "posts_home.html"
