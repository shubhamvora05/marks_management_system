from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm
from marksApp.models import studentInfo, Standerd, subject, Marks, marksRecord
from marksApp.forms import standerdForm, subjectForm, studentForm, marksForm
from django.forms import formset_factory
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

# userhome handling


def userHome(request):

    stdForm = standerdForm()
    if request.POST.get("deleteStanderd"):
        Standerd.objects.filter(Id=request.POST.get("deleteStanderd")).delete()

    if request.POST.get("AddNewStanderd"):
        form = standerdForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    if request.POST.get("updateStanderd"):

        currentStanderd = Standerd.objects.get(
            Id=request.POST.get("updateStanderd"))

        formToUpdate = standerdForm(
            request.POST or None, instance=currentStanderd)
        if formToUpdate.is_valid():
            formToUpdate.save()

    allStanderd = Standerd.objects.all()
    context = {'allStanderd': allStanderd, 'standerdForm': stdForm}
    return render(request, 'MarksApp/home.html', context)

# standerd page handling function


def standerdHandling(request, StanderdId):

    subForm = subjectForm()
    stdForm = studentForm()

    # subject handling

    if request.POST.get("deleteSubject"):
        subject.objects.filter(id=request.POST.get("deleteSubject")).delete()

    if request.POST.get("AddNewSubject"):
        form = subjectForm(request.POST)
        if form.is_valid():
            fromSave = form.save(commit=False)
            fromSave.subjectStd = Standerd.objects.get(Id=StanderdId)
            fromSave.save()
        return redirect('/'+str(StanderdId))

    if request.POST.get("updateSubject"):

        currentSubject = subject.objects.get(
            id=request.POST.get("updateSubject"))

        formToUpdate = subjectForm(
            request.POST or None, instance=currentSubject)
        if formToUpdate.is_valid():
            formToUpdate.save()

    # student handling

    if request.POST.get("deleteStudent"):
        studentInfo.objects.filter(
            HR_No=request.POST.get("deleteStudent")).delete()

    if request.POST.get("AddNewStudent"):
        form = studentForm(request.POST)
        if form.is_valid():
            fromSave = form.save(commit=False)
            fromSave.studentStd = Standerd.objects.get(Id=StanderdId)
            fromSave.save()

    if request.POST.get("updateStudent"):

        currentSubject = studentInfo.objects.get(
            HR_No=request.POST.get("updateStudent"))

        formToUpdate = studentForm(
            request.POST or None, instance=currentSubject)
        if formToUpdate.is_valid():
            formToUpdate.save()

    allSubject = subject.objects.filter(subjectStd=StanderdId)
    allStudent = studentInfo.objects.filter(studentStd=StanderdId)

    context = {'allSubject': allSubject, 'subjectForm': subForm,
               'StanderdId': StanderdId, 'studentForm': stdForm, 'allStudent': allStudent, }

    return render(request, 'MarksApp/standerdDetails.html', context)


def subjectHandling(request, StanderdId, subjectId):

    allStudent = studentInfo.objects.filter(studentStd=StanderdId)
    currentSubject = subject.objects.get(id=subjectId)
    currentStanderd = Standerd.objects.get(Id=StanderdId)

    if request.POST.get("AddNewMarksRecord"):
        TotalMarks = request.POST['TotalMarks']
        CurrentDate = request.POST['CurrentDate']

        marksObject = marksRecord.objects.create(
            totalMarks=TotalMarks, date=CurrentDate, Subject=currentSubject)
        marksObject.save()

    if request.POST.get("deleteMarksRecord"):
        marksRecord.objects.filter(
            Id=request.POST.get("deleteMarksRecord")).delete()

    if request.POST.get("updateMarksRecord"):
        TotalMarks = request.POST['TotalMarks']
        CurrentDate = request.POST['CurrentDate']

        marksRecord.objects.filter(Id=request.POST.get(
            "updateMarksRecord")).update(totalMarks=TotalMarks, date=CurrentDate)

    AllMarksRecords = marksRecord.objects.filter(Subject=subjectId)

    context = {'Subject': currentSubject,
               'Standerd': currentStanderd, 'marksRecords': AllMarksRecords, }

    return render(request, 'MarksApp/subjectDetails.html', context)

# update and add the marks of the student in particuler subject record


def addAndupdateMarks(request, StanderdId, subjectId, marksrecordId):

    allStudent = studentInfo.objects.filter(studentStd=StanderdId)
    currentSubject = subject.objects.get(id=subjectId)
    currentStanderd = Standerd.objects.get(Id=StanderdId)
    currentRecord = marksRecord.objects.get(Id=marksrecordId)

    if request.POST.get("AddMarksStudent"):

        MarksRecordToAdd = marksRecord.objects.get(
            Id=request.POST['AddMarksStudent'])
        marksWithCurrentRecord = Marks.objects.filter(
            totalMarks=MarksRecordToAdd)

        # code to update added marks
        if marksWithCurrentRecord.exists():
            for student in allStudent:
                x = 'AchivedMarks' + student.HR_No
                achivedMarks = request.POST[x]
                marksToUpdate = Marks.objects.get(
                    Student=student, totalMarks=MarksRecordToAdd)
                marksToUpdate.achivedMarks = achivedMarks
                marksToUpdate.save()

        # code to add new marks
        else:

            for student in allStudent:
                x = 'AchivedMarks' + student.HR_No
                achivedMarks = request.POST[x]
                MarksObject = Marks.objects.create(
                    achivedMarks=achivedMarks, Student=student, totalMarks=MarksRecordToAdd)
                MarksObject.save()

    marks_list = []

    for student in allStudent:
        try:
            marksOfStudent = Marks.objects.get(
                Student=student, totalMarks=marksrecordId)
            marks_list.append(marksOfStudent)
        except:
            marks_list.append(None)
            print("object is not in the list")

    context = {'allStudentAndMarks': zip(allStudent, marks_list), 'allStudent': allStudent, 'Subject': currentSubject,
               'Standerd': currentStanderd, 'Record': currentRecord}

    return render(request, 'MarksApp/studentAddandUpdateMakrs.html', context)
