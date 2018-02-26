# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import User, UserManager
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'LoginReg3_app/index.html')

def register(request):
    results = User.objects.validateRegister(request.POST)

    if not results['status']:
        genErrorMessages(request, results)
        return redirect('/')
    else:
        newUser = User.objects.createUser(request.POST)
        genSessions(request, newUser)
        return redirect('/dashboard')

def login(request):
    results = User.objects.validateLogin(request.POST)

    if not results['user']:
        genErrorMessages(request, results)
        return redirect('/')
    else:
        genSessions(request, results['user'])
        return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

########################### Helper Methods
def genErrorMessages(request, results):
    for error in results['errors']:
        messages.error(request, error)

def genSessions(request, curUser):
    request.session['userID'] = curUser.id