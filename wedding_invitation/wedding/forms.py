from django import forms
from .models import RSVP, GuestbookEntry


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'phone', 'attendance', 'guests', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Votre nom et prénom',
                'class': 'mt-2 input-field',
                'autocomplete': 'name',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+237 ...',
                'class': 'mt-2 input-field',
                'autocomplete': 'tel',
            }),
            'attendance': forms.Select(attrs={
                'class': 'mt-2 input-field bg-[#071120]',
            }),
            'guests': forms.NumberInput(attrs={
                'min': 1,
                'max': 10,
                'class': 'mt-2 input-field',
            }),
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Un mot, une bénédiction ou une contrainte alimentaire...',
                'class': 'mt-2 input-field',
            }),
        }
        labels = {
            'name': 'Nom complet',
            'phone': 'Téléphone',
            'attendance': 'Présence',
            'guests': "Nombre d'invités",
            'message': 'Message aux mariés',
        }


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Votre nom',
                'class': 'mt-2 input-field',
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Votre message pour Jocelyne et Prosper',
                'class': 'mt-2 input-field',
            }),
        }
        labels = {
            'name': 'Votre nom',
            'message': 'Votre message',
        }
