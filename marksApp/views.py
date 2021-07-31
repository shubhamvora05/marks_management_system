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
    try:
        stdForm = standerdForm()
        if request.POST.get("deleteStanderd"):
            msgStd = Standerd.objects.get(
                Id=request.POST.get("deleteStanderd"))
            messages.info(request, "Standerd" + str(msgStd.Std) + " " +
                          str(msgStd.Div) + " " + str(msgStd.Medium) + " deleted successfully.")
            Standerd.objects.filter(
                Id=request.POST.get("deleteStanderd")).delete()
            return redirect("/")

        if request.POST.get("AddNewStanderd"):
            form = standerdForm(request.POST)
            if form.is_valid():
                form.save()
            messages.info(request, "New standerd is added successfully.")
            return redirect("/")

        if request.POST.get("updateStanderd"):

            currentStanderd = Standerd.objects.get(
                Id=request.POST.get("updateStanderd"))
            std = currentStanderd.Std
            medium = currentStanderd.Medium
            div = currentStanderd.Div

            formToUpdate = standerdForm(
                request.POST or None, instance=currentStanderd)
            if formToUpdate.is_valid():
                formToUpdate.save()

            messages.info(request, str(std) + " " + str(div) + " "+str(medium) +
                          " is updated to " + str(currentStanderd .Std)+" "+str(currentStanderd .Div)+" "+str(currentStanderd .Medium))
            return redirect("/")

        allStanderd = Standerd.objects.all()
        context = {'allStanderd': allStanderd, 'standerdForm': stdForm}
        return render(request, 'MarksApp/home.html', context)

    except:
        return render(request, 'MarksApp/error.html')


# standerd page handling function


def standerdHandling(request, StanderdId):

    try:
        subForm = subjectForm()
        stdForm = studentForm()

    # subject handling

        if request.POST.get("deleteSubject"):
            msgsub = subject.objects.get(id=request.POST.get("deleteSubject"))
            messages.info(request, str(msgsub.subject_Name) +
                          " is deleted successfully")
            subject.objects.filter(
                id=request.POST.get("deleteSubject")).delete()
            return redirect("/"+str(StanderdId))

        if request.POST.get("AddNewSubject"):
            form = subjectForm(request.POST)
            if form.is_valid():
                fromSave = form.save(commit=False)
                fromSave.subjectStd = Standerd.objects.get(Id=StanderdId)
                fromSave.save()
            messages.info(request, "New subject added successfully")
            return redirect('/'+str(StanderdId))

        if request.POST.get("updateSubject"):

            currentSubject = subject.objects.get(
                id=request.POST.get("updateSubject"))
            currsub = currentSubject.subject_Name

            formToUpdate = subjectForm(
                request.POST or None, instance=currentSubject)
            if formToUpdate.is_valid():
                formToUpdate.save()

            messages.info(request, str(currsub) +
                          " is updated to "+str(currentSubject.subject_Name))
            return redirect('/'+str(StanderdId))

    # student handling

        if request.POST.get("deleteStudent"):
            msgstudent = studentInfo.objects.get(
                id=request.POST.get("deleteStudent"))
            messages.info(request, str(msgstudent.first_name)+" "+str(msgstudent.Middle_name) +
                          " "+str(msgstudent.Last_name)+" is deleted successfully")
            studentInfo.objects.filter(
                id=request.POST.get("deleteStudent")).delete()
            return redirect('/'+str(StanderdId))

        if request.POST.get("AddNewStudent"):
            form = studentForm(request.POST)
            if form.is_valid():
                fromSave = form.save(commit=False)
                fromSave.studentStd = Standerd.objects.get(Id=StanderdId)
                fromSave.save()
            messages.info(request, "New student is added successfully")
            return redirect('/'+str(StanderdId))

        if request.POST.get("updateStudent"):

            currentSubject = studentInfo.objects.get(
                id=request.POST.get("updateStudent"))

            formToUpdate = studentForm(
                request.POST or None, instance=currentSubject)
            if formToUpdate.is_valid():
                formToUpdate.save()
            messages.info(request, "Student is updated successfully.")
            return redirect('/'+str(StanderdId))

        allSubject = subject.objects.filter(subjectStd=StanderdId)
        allStudent = studentInfo.objects.filter(studentStd=StanderdId)
        currentStanderd = Standerd.objects.get(Id=StanderdId)

        context = {'currentStanderd': currentStanderd, 'allSubject': allSubject, 'subjectForm': subForm,
                   'StanderdId': StanderdId, 'studentForm': stdForm, 'allStudent': allStudent, }

        return render(request, 'MarksApp/standerdDetails.html', context)

    except:
        return render(request, 'MarksApp/error.html')


def subjectHandling(request, StanderdId, subjectId):
    try:
        allStudent = studentInfo.objects.filter(studentStd=StanderdId)
        currentSubject = subject.objects.get(id=subjectId)
        currentStanderd = Standerd.objects.get(Id=StanderdId)

        if request.POST.get("AddNewMarksRecord"):
            TotalMarks = request.POST['TotalMarks']
            CurrentDate = request.POST['CurrentDate']

            marksObject = marksRecord.objects.create(
                totalMarks=TotalMarks, date=CurrentDate, Subject=currentSubject)
            marksObject.save()
            messages.info(request, "New record added successfully")
            return redirect("/"+str(StanderdId)+"/"+str(subjectId))

        if request.POST.get("deleteMarksRecord"):

            messages.info(request, "Marks record deleted successfully.")
            marksRecord.objects.filter(
                Id=request.POST.get("deleteMarksRecord")).delete()
            return redirect("/"+str(StanderdId)+"/"+str(subjectId))

        if request.POST.get("updateMarksRecord"):
            TotalMarks = request.POST['TotalMarks']
            CurrentDate = request.POST['CurrentDate']

            marksRecord.objects.filter(Id=request.POST.get(
                "updateMarksRecord")).update(totalMarks=TotalMarks, date=CurrentDate)
            messages.info(request, "marks record updated successfully.")
            return redirect("/"+str(StanderdId)+"/"+str(subjectId))

        AllMarksRecords = marksRecord.objects.filter(Subject=subjectId)

        context = {'Subject': currentSubject,
                   'Standerd': currentStanderd, 'marksRecords': AllMarksRecords, }

        return render(request, 'MarksApp/subjectDetails.html', context)
    except:
        return render(request, 'MarksApp/error.html')
# update and add the marks of the student in particuler subject record


def addAndupdateMarks(request, StanderdId, subjectId, marksrecordId):

    try:

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
            messages.info(request, "Marks of Students updated successfully.")
            return redirect("/"+str(StanderdId)+"/" + str(subjectId)+"/" + str(marksrecordId))

        marks_list = []

        for student in allStudent:
            try:
                marksOfStudent = Marks.objects.get(
                    Student=student, totalMarks=marksrecordId)
                marks_list.append(marksOfStudent)
            except:
                marks_list.append(None)

        context = {'allStudentAndMarks': zip(allStudent, marks_list), 'allStudent': allStudent, 'Subject': currentSubject,
                   'Standerd': currentStanderd, 'Record': currentRecord}

        return render(request, 'MarksApp/studentAddandUpdateMakrs.html', context)

    except:
        return render(request, 'MarksApp/error.html')
