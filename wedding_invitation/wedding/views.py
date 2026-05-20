from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RSVPForm, GuestbookForm
from .models import GuestbookEntry, GalleryPhoto


def rsvp(request):
    """Affiche et traite le formulaire de confirmation de présence."""
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci ! Votre réponse a bien été enregistrée.")
            return redirect('rsvp')
    else:
        form = RSVPForm()
    return render(request, 'wedding/rsvp.html', {'form': form})


def guestbook(request):
    """Affiche le livre d'or et traite les nouveaux messages."""
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci pour votre message !")
            return redirect('guestbook')
    else:
        form = GuestbookForm()
    entries = GuestbookEntry.objects.all()
    return render(request, 'wedding/guestbook.html', {'form': form, 'entries': entries})


def gallery(request):
    """Affiche la galerie photos (images admin si disponibles, sinon placeholder)."""
    photos = GalleryPhoto.objects.all()
    return render(request, 'wedding/gallery.html', {'photos': photos})
