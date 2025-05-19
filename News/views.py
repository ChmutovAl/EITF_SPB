from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, View

from EITF_SPB.settings import DEFAULT_FROM_EMAIL
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


class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        if kwargs.get('embedded'):
            return render(request, '_feedback_form.html', {'form': form})
        return render(request, 'contact_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fio = f'{form.cleaned_data["last_name"]}  {form.cleaned_data["name"]}'
            type = f'{form.cleaned_data["type"]}'
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            body_msg = form.cleaned_data['message']
            message = (f'Отправитель: {fio} \n'
                       f'Email: {email} \n'
                       f'Телефон: {phone} \n'
                       f'Тип отправителя: {type} \n'
                       f'Вопрос: {body_msg}')
            send_mail(
                subject='Обратная связь',
                message=message,
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=['chmutov.aleks@yandex.ru', 'tkdspb_eitf@mail.ru']
            )
            return HttpResponseRedirect(reverse_lazy('home'))
        if kwargs.get('embedded'):
            return render(request, '_feedback_form.html', {'form': form})
        return render(request, 'contact_form.html', {'form': form})

    @classmethod
    def as_view(cls, **initkwargs):
        embedded = initkwargs.pop('embedded', False)
        view = super().as_view(**initkwargs)
        view.embedded = embedded  # Устанавливаем атрибут класса
        return view

# class ContactFormView(FormView):
#     form_class = FeedbackForm
#     template_name = 'contact_form.html'
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         fio = f'{form.cleaned_data["last_name"]}  {form.cleaned_data["name"]}'
#         type = f'{form.cleaned_data["type"]}'
#         email = form.cleaned_data['email']
#         phone = form.cleaned_data['phone']
#         body_msg = form.cleaned_data['message']
#         message = (f'Отправитель: {fio} \n'
#                    f'Email: {email} \n'
#                    f'Телефон: {phone} \n'
#                    f'Тип отправителя: {type} \n'
#                    f'Вопрос: {body_msg}')
#         send_mail(
#             subject ='Обратная связь',
#             message = message,
#             from_email = DEFAULT_FROM_EMAIL,
#             recipient_list=['chmutov.aleks@yandex.ru',]
#         )
#         return super().form_valid(form)