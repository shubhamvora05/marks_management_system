from django.contrib import admin
from marksApp.models import studentInfo,Standerd, subject, Marks

# Register your models here.
models = (studentInfo,Standerd, subject, Marks)
for m in models:
   admin.site.register(m)