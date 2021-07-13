from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm
from marksApp.models import studentInfo,Standerd, subject, Marks
from marksApp.forms import standerdForm, subjectForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

#userhome handling
def userHome(request):

    stdForm = standerdForm()

    if request.POST.get("deleteStanderd"):
        Standerd.objects.filter(Id=request.POST.get("deleteStanderd")).delete()


    if request.POST.get("AddNewStanderd"):
        form = standerdForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    allStanderd = Standerd.objects.all()
    context={'allStanderd':allStanderd,'standerdForm':stdForm }
    return render(request, 'MarksApp/home.html',context)

def standerdHandling(request,StanderdId):

    subForm = subjectForm()

    if request.POST.get("deleteSubject"):
        subject.objects.filter(id=request.POST.get("deleteSubject")).delete()


    if request.POST.get("AddNewSubject"):
        form = subjectForm(request.POST)
        if form.is_valid():
            fromSave=form.save(commit=False)
            fromSave.subjectStd = Standerd.objects.get(Id=StanderdId)
            fromSave.save()
        return redirect('/'+str(StanderdId))

    allSubject = subject.objects.filter(subjectStd=StanderdId)
    context={'allSubject':allSubject,'subjectForm':subForm,'StanderdId':StanderdId } 
    return render(request, 'MarksApp/standerdDetails.html',context)