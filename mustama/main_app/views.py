from django.shortcuts import render

from .models import Recitation

# Create your views here.


def home(request):
    return render (request,'home.html')


def about(request):
    return render(request,'app/about.html')


def record_index(request):
    records=Recitation.objects.filter(approval=True)
    return render(request,'record/index.html',{'records':records})


def record_myRecord(request):
    records=Recitation.objects.all()
    return render(request,'record/myRecord.html',{'records':records}) 