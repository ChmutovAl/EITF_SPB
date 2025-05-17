from django import forms
from .models import *

class FeedbackForm(forms.Form):
    last_name = forms.CharField(max_length=120)
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    type = forms.ChoiceField()
    message = forms.CharField(widget=forms.Textarea)