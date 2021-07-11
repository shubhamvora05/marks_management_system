from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm
#from user.models import 
#from user.forms import 
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

#userhome handling
def userHome(request):
    return HttpResponse("marks management system")