from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Recitation
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def home(request):
    return render (request,'home.html')


def about(request):
    return render(request,'app/about.html')


def record_index(request):
    records=Recitation.objects.filter(approval=True)
    return render(request,'record/index.html',{'records':records})


def record_myRecord(request):
    records=Recitation.objects.filter(user=request.user)
    return render(request,'record/myRecord.html',{'records':records}) 
class RecitationCreate(CreateView):
    model=Recitation
    fields=['surahName','Reciter','reciterImage','audio']
    success_url='/record/myRecord/'
def signup(request):
    error_message=""
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            login(request,user)
            return redirect('index')
        else:
            error_message='Invalid Signup - Try Again'
    form=UserCreationForm()
    context={'form':form,'error_message':error_message}
    return render(request,'registration/signup.html',context)