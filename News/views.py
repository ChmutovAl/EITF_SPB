from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .forms import FeedbackForm
from .models import *


class PostListView(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 9


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ContactFormView(FormView):
    form_class = FeedbackForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('home')