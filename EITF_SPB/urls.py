"""
URL configuration for EITF_SPB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from News.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('о-нас/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('новости/', PostListView.as_view(), name='news'),
    path('новости/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('контакты/', FeedbackView.as_view(), name='contacts'),
    path('обратная-связь/', FeedbackView.as_view(embedded=True), name='feedback')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)