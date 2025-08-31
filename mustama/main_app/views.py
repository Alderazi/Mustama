from django.shortcuts import render

from .models import Recitation

# Create your views here.
def home(request):
    return render (request,'home.html')
def about(request):
    return render(request,'app/about.html')
def record_index(request):
    records=Recitation.objects.all()
    return render(request,'record/index.html',{'records':records})