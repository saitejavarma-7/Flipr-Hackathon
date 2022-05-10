# from django.http import request
from django.shortcuts import render

from .models import Profile

from .forms import Registration

# Create your views here.
def home(request):
    return render(request,'base.html')
def register(request):
    if request.method=="POST":
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            id = form.cleaned_data['id']
            aadhar = form.cleaned_data['aadhar']
            pancard = form.cleaned_data['pancard']
            salary = form.cleaned_data['salary']
            photo = form.cleaned_data['photo']
            bank = form.cleaned_data['bank']
            ctc = form.cleaned_data['ctc']
            loan = form.cleaned_data['loan']
            p = Profile.objects.all()
            p.save({'name':name,'id':id,'aadhar':aadhar,'pancard':pancard,'salary':salary,'photo':photo,'bank':bank,'ctc':ctc,'loan':loan})
            return render(request,'login.html')
    else:
        form = Registration()
    return render(request,"registration.html",{'form':form})


