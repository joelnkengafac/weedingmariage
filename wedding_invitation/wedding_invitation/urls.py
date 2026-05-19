"""
URL configuration for wedding_invitation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='wedding/home.html'), name='home'),
    path('story/', TemplateView.as_view(template_name='wedding/story.html'), name='story'),
    path('programme/', TemplateView.as_view(template_name='wedding/programme.html'), name='programme'),
    path('gallery/', TemplateView.as_view(template_name='wedding/gallery.html'), name='gallery'),
    path('rsvp/', TemplateView.as_view(template_name='wedding/rsvp.html'), name='rsvp'),
    path('dresscode/', TemplateView.as_view(template_name='wedding/dresscode.html'), name='dresscode'),
    path('gifts/', TemplateView.as_view(template_name='wedding/gifts.html'), name='gifts'),
    path('guestbook/', TemplateView.as_view(template_name='wedding/guestbook.html'), name='guestbook'),
    path('livestream/', TemplateView.as_view(template_name='wedding/livestream.html'), name='livestream'),
    path('contact/', TemplateView.as_view(template_name='wedding/contact.html'), name='contact'),
    path('admin/', admin.site.urls),
]
