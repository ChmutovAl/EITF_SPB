from django import template
from ..models import *
from ..forms import *

register = template.Library()

@register.inclusion_tag('_staff.html')
def show_staff():
    staff = Staff.objects.all()
    return {'staff': staff}

@register.inclusion_tag('_posts.html')
def show_posts(count=2):
    posts = Post.objects.all()[:count]
    return {'posts': posts}

@register.inclusion_tag('_footer_posts.html')
def show_footer_posts(count=4):
    posts = Post.objects.all()[:count]
    return {'posts': posts}

@register.inclusion_tag('_feedback_form.html')
def show_feedback_form():
    feedback = FeedbackForm
    return {'form':feedback}

@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })