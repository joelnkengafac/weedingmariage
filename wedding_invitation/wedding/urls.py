from django.urls import path
from . import views

urlpatterns = [
    path('rsvp/', views.rsvp, name='rsvp'),
    path('guestbook/', views.guestbook, name='guestbook'),
    path('gallery/', views.gallery, name='gallery'),
]
