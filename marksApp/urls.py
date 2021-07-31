from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("", views.userHome, name='Home'),
    path("<int:StanderdId>", views.standerdHandling, name='StanderdHandling'),
    path("<str:StanderdId>/<str:subjectId>",
         views.subjectHandling, name='subjectHandling'),
    path("<str:StanderdId>/<str:subjectId>/<str:marksrecordId>",
         views.addAndupdateMarks, name='addAndupdateMarks'),
]
