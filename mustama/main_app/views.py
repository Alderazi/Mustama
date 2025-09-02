from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Recitation
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




# Create your views here.
class RecordCreate(LoginRequiredMixin, CreateView):
    model = Recitation
    fields = ['surahName', 'Reciter', 'reciterImage', 'audio']
    success_url = '/record/myRecord/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class RecordUpdate(LoginRequiredMixin,UpdateView):
    model=Recitation
    fields=['surahName','Reciter','reciterImage',"audio"]
    success_url = '/record/index/'
class RecordDelete(LoginRequiredMixin,DeleteView):
    model=Recitation
    success_url='/record/index/'
def home(request):
    return render (request,'home.html')


def about(request):
    return render(request,'app/about.html')


def record_index(request):
    records=Recitation.objects.filter(approval='APPROVED')
    return render(request,'record/index.html',{'records':records})

@login_required(login_url='/accounts/login/')
def record_myRecord(request):
    records = Recitation.objects.filter(user=request.user)
    return render(request, 'record/myRecord.html', {'records': records})


def approval(request):
    records=Recitation.objects.filter(approval='PENDING')
    return render(request,'adminPage/approval.html',{'records':records})


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
def approve(request,record_id):
    record = Recitation.objects.get(id=record_id)
    record.approval = 'APPROVED'
    record.save()
    return redirect('approval')

def reject(request,record_id):
    record = Recitation.objects.get(id=record_id)
    record.approval = 'REJECTED'
    record.save()
    return redirect('approval')
