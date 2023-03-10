# Generated by Django 4.1.3 on 2023-01-17 11:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='', verbose_name='Illustration')),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True, verbose_name='titre')),
                ('image', models.ImageField(upload_to='', verbose_name='Illustration')),
                ('audio_file', models.FileField(upload_to='audio', validators=[django.core.validators.FileExtensionValidator(['mp3', 'm4a', 'aac', 'wav'])], verbose_name='fichier audio')),
                ('genre', models.CharField(choices=[('RNB', 'RNB'), ('GOSPEL', 'Gospel'), ('RAP', 'RAP'), ('TRADITIONAL', 'Musique Traditonnel'), ('LOVE', 'Amour'), ('NOSTALGIA', 'Nostalgie')], max_length=40, verbose_name='Genre_musical')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('price', models.CharField(choices=[('2000 Fcfa', '2000 Fcfa'), ('3000 Fcfa', '3000 Fcfa'), ('4000 Fcfa', '4000 Fcfa'), ('5000 Fcfa', '5000 Fcfa'), ('6000 Fcfa', '6000 Fcfa'), ('10000 Fcfa', '10000 Fcfa')], max_length=60, verbose_name='Votre Prix')),
                ('albums', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.album', verbose_name='album')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Chanteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=4000, verbose_name='Suggestion')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('network', models.CharField(max_length=50)),
                ('tx_reference', models.CharField(max_length=200)),
                ('article', models.ManyToManyField(blank=True, to='music.music', verbose_name='Acticle')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Acheteur')),
            ],
        ),
        migrations.CreateModel(
            name='MusicDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='audio', validators=[django.core.validators.FileExtensionValidator(['mp3', 'm4a', 'aac', 'wav'])])),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demo', to='music.music')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='musics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='musics', to='music.music'),
        ),
    ]
