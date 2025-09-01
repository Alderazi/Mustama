from django.db import models
from django.contrib.auth.models import User
# Create your models here.
APPROVAL=(
    ('APPROVED','Approved'),
    ('PENDING','Pending'),
    ('REJECTED','Rejected'),
)
class Recitation(models.Model):
    surahName=models.CharField(max_length=30)
    Reciter=models.CharField(max_length=100)
    reciterImage=models.ImageField(upload_to='main_app/static/uploads/pictures',default="main_app/static/uploads/pictures/default.jpeg")
    audio=models.FileField(upload_to='main_app/static/uploads/audio')
    approval=models.CharField(choices=APPROVAL,default=APPROVAL[1][0])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
