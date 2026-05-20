from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from wedding import views as wedding_views

urlpatterns = [
    # Pages statiques
    path('', TemplateView.as_view(template_name='wedding/home.html'), name='home'),
    path('story/', TemplateView.as_view(template_name='wedding/story.html'), name='story'),
    path('programme/', TemplateView.as_view(template_name='wedding/programme.html'), name='programme'),
    path('dresscode/', TemplateView.as_view(template_name='wedding/dresscode.html'), name='dresscode'),
    path('gifts/', TemplateView.as_view(template_name='wedding/gifts.html'), name='gifts'),
    path('livestream/', TemplateView.as_view(template_name='wedding/livestream.html'), name='livestream'),
    path('contact/', TemplateView.as_view(template_name='wedding/contact.html'), name='contact'),

    # Pages avec logique backend
    path('rsvp/', wedding_views.rsvp, name='rsvp'),
    path('guestbook/', wedding_views.guestbook, name='guestbook'),
    path('gallery/', wedding_views.gallery, name='gallery'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)