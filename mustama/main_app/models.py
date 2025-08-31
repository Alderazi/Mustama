from django.db import models

# Create your models here.
class Recitation(models.Model):
    surahName=models.CharField(max_length=30)
    Reciter=models.CharField(max_length=100)
    reciterImage=models.ImageField(upload_to='main_app/static/uploads/pictures',default="")
    audio=models.FileField(upload_to='main_app/static/uploads/audio',)