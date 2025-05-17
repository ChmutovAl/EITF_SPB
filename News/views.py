from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class PostListView(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 9
