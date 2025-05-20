from django import forms
from .models import *

class FeedbackForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    name = forms.CharField(label='Имя', max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label='Телефон', max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    type = forms.ChoiceField(choices=(('Спортивный клуб', 'Спортивный клуб'), ('Инструктор', 'Инструктор'), ('Спортсмен', 'Спортсмен')))
    message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'placeholder':'Напишите более подробную информацию или свой вопрос'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'about', 'content', 'banner']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'about':forms.Textarea(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'banner':forms.FileInput(attrs={'class':'form-control'}),
        }
