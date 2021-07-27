from django import forms
from marksApp.models import studentInfo, Standerd, subject, Marks, marksRecord


class standerdForm(forms.ModelForm):
    class Meta:
        model = Standerd
        fields = ('Std', 'Medium', 'Div',)


class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ('subject_Name',)


class studentForm(forms.ModelForm):
    class Meta:
        model = studentInfo
        fields = ('HR_No', 'first_name', 'Middle_name',
                  'Last_name', 'Room_No',)


class marksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ('achivedMarks',)
