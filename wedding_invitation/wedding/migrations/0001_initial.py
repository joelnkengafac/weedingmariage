from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom complet')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Téléphone')),
                ('attendance', models.CharField(
                    choices=[('yes', 'Je serai présent(e)'), ('no', 'Je ne pourrai pas venir')],
                    max_length=3,
                    verbose_name='Présence',
                )),
                ('guests', models.PositiveSmallIntegerField(default=1, verbose_name="Nombre d'invités")),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Reçu le')),
            ],
            options={
                'verbose_name': 'RSVP',
                'verbose_name_plural': 'RSVPs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GuestbookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Publié le')),
            ],
            options={
                'verbose_name': "Message du livre d'or",
                'verbose_name_plural': "Messages du livre d'or",
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Photo')),
                ('caption', models.CharField(blank=True, max_length=200, verbose_name='Légende')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Photo de galerie',
                'verbose_name_plural': 'Photos de galerie',
                'ordering': ['order', 'id'],
            },
        ),
    ]
