from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recitation(models.Model):
    surahName=models.CharField(max_length=30)
    Reciter=models.CharField(max_length=100)
    reciterImage=models.ImageField(upload_to='main_app/static/uploads/pictures',default="")
    audio=models.FileField(upload_to='main_app/static/uploads/audio')
    approval=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
