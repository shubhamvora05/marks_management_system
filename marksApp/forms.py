from django import forms
from marksApp.models import studentInfo,Standerd, subject, Marks


class standerdForm(forms.ModelForm):
    class Meta:
        model = Standerd
        fields = ('Std','Medium','Div',)