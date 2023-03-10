from django.db import models
from authentication.models import *
import mutagen
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save, post_save
from pydub import AudioSegment
from django.dispatch import receiver


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=60)
    Author = models.ForeignKey(User, on_delete= models.SET_NULL, related_name='created_by', null=True)
    image = models.ImageField(verbose_name='Illustration')
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    musics = models.ForeignKey('Music', on_delete=models.SET_NULL, related_name='musics', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Music(models.Model):
    RNB = 'RNB'
    GOSPEL = 'GOSPEL'
    RAP = 'RAP'
    TRADITIONAL = 'TRADITIONAL'
    LOVE = 'LOVE'
    NOSTALGIA = 'NOSTALGIA'

    GENRE_CHOICES = (
        (RNB, 'RNB'),
        (GOSPEL, 'Gospel'),
        (RAP, 'RAP'),
        (TRADITIONAL, 'Musique Traditonnel'),
        (LOVE, 'Amour'),
        (NOSTALGIA, 'Nostalgie')
    )
    PRICE_CHOICES = (
        ('2000 Fcfa', '2000 Fcfa'),
        ('3000 Fcfa', '3000 Fcfa'),
        ('4000 Fcfa', '4000 Fcfa'),
        ('5000 Fcfa', '5000 Fcfa'),
        ('6000 Fcfa', '6000 Fcfa'),
        ('10000 Fcfa','10000 Fcfa'),
    )

    title = models.CharField(verbose_name='titre', unique=True, max_length=60)
    creator = models.ForeignKey(User, null=True, related_name="Chanteur", blank=True, on_delete=models.SET_NULL)
    albums = models.ForeignKey(Album, on_delete=models.SET_NULL, verbose_name='album', null=True, blank=True)
    image = models.ImageField(verbose_name='Illustration')
    audio_file = models.FileField(upload_to="audio", blank=False, verbose_name='fichier audio', validators=[FileExtensionValidator(['mp3', 'm4a', 'aac', 'wav',])])
    genre = models.CharField(max_length=40,choices=GENRE_CHOICES, verbose_name='Genre_musical')
    date_created = models.DateField(auto_now_add=True)
    price = models.CharField(choices=PRICE_CHOICES, verbose_name='Votre Prix', max_length=60)

    

    def __str__(self):
        return str(self.title)



    '''
    auth_token	Jeton d???authentification de l???e-commerce (Cl?? API)	OUI
    phone_number	Num??ro de t??l??phone mobile du Client	OUI
    amount	Montant de la transaction sans la devise (Devise par d??faut: FCFA)	OUI
    description	D??tails de la transaction	NON
    identifier	Identifiant interne de la transaction de l???e-commerce. Cet identifiant doit etre unique.	OUI
    network
    '''
class Order(models.Model):
    customer = models.ForeignKey(User, verbose_name='Acheteur',  on_delete=models.CASCADE, primary_key=False, unique=False)
    article = models.ManyToManyField(Music, verbose_name='Acticle',blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # Let Test this and see the outcome :
    status = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    tx_reference = models.CharField(max_length=200)

    def place_order(self):
        self.save()


    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer= customer_id)


class MusicDemo(models.Model):
    music = models.ForeignKey(Music,related_name="demo", on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="audio", validators=[FileExtensionValidator(['mp3', 'm4a', 'aac', 'wav',])])

class Suggestion(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    content = models.TextField(verbose_name='Suggestion', max_length=4000)
    date_created = models.DateField(auto_now_add=True)



@receiver(post_save, sender=Music)
def create_demo(sender, instance, created, **kwargs):
    if not created:
        return False
    audio_file = instance.audio_file.path
    audio = AudioSegment.from_file(audio_file)
    demo_audio = audio[:30000]
    demo_file_name = f"{instance.title}_demo.mp3"
    demo_audio.export(demo_file_name, format='mp3')
    if not MusicDemo.objects.filter(music=instance).exists():
        MusicDemo.objects.create(
            music=instance,
            audio_file=demo_file_name
        )
