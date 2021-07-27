from django.contrib import admin
from marksApp.models import studentInfo, Standerd, subject, Marks, marksRecord

# Register your models here.
models = (studentInfo, Standerd, subject, Marks, marksRecord)
for m in models:
    admin.site.register(m)
