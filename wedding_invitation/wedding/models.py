from django.db import models


class RSVP(models.Model):
    ATTENDANCE_CHOICES = [
        ('yes', 'Je serai présent(e)'),
        ('no', 'Je ne pourrai pas venir'),
    ]
    name = models.CharField(max_length=150, verbose_name="Nom complet")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    attendance = models.CharField(
        max_length=3,
        choices=ATTENDANCE_CHOICES,
        verbose_name="Présence",
    )
    guests = models.PositiveSmallIntegerField(default=1, verbose_name="Nombre d'invités")
    message = models.TextField(blank=True, verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Reçu le")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'RSVP'
        verbose_name_plural = 'RSVPs'

    def __str__(self):
        return f"{self.name} — {self.get_attendance_display()}"


class GuestbookEntry(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nom")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Publié le")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Message du livre d'or"
        verbose_name_plural = "Messages du livre d'or"

    def __str__(self):
        return f"{self.name} — {self.created_at.strftime('%d/%m/%Y')}"


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Photo")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Légende")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Photo de galerie'
        verbose_name_plural = 'Photos de galerie'

    def __str__(self):
        return self.caption or f"Photo {self.id}"
