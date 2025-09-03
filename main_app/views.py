from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Recitation
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required




# Create your views here.
class RecordCreate(LoginRequiredMixin, CreateView):
    model = Recitation
    fields = ['surahName', 'Reciter', 'reciterImage','description', 'audio']
    success_url = '/record/myRecord/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        if(self.request.user.is_staff):
            form.instance.approval="APPROVED"
        return super().form_valid(form)
class RecordUpdate(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Recitation
    fields=['surahName','Reciter','reciterImage',"description","audio"]
    success_url = '/record/index/'
    def test_func(self):
        return self.request.user.is_staff
    
class RecordDelete(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Recitation
    success_url='/record/index/'
    def test_func(self):
        return self.request.user.is_staff
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

@login_required
def approval(request):
    if(request.user.is_staff):
        records=Recitation.objects.filter(approval='PENDING')
        return render(request,'adminPage/approval.html',{'records':records})
    else:
        return redirect('home')

def signup(request):
    error_message=""
    if (request.method=='POST'):
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
@login_required
def approve(request,record_id):
    if(request.user.is_staff):
        record = Recitation.objects.get(id=record_id)
        record.approval = 'APPROVED'
        record.save()
        return redirect('approval')
    else:
        return redirect('home')
@login_required
def reject(request,record_id):
    if(request.user.is_staff):
        record = Recitation.objects.get(id=record_id)
        record.approval = 'REJECTED'
        record.save()
        return redirect('approval')
    else:
        return redirect('home')
def info(request):
    records = Recitation.objects.filter(approval='APPROVED')
    unique_records = checkDuplicated(records)
    return render(request, 'app/info.html', {'records': unique_records})

def checkDuplicated(records):
    uniqueValues = []
    for i in records:
        duplicatedFlag = False
        for j in uniqueValues:
            if i.Reciter == j.Reciter:
                duplicatedFlag = True
                break
        if not duplicatedFlag:
            uniqueValues.append(i)
    return uniqueValues
