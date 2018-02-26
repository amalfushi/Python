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
        # newUser = User.objects.createUser(request.POST)
        return HttpResponse('Registered!')

def login(request):
    return HttpResponse('Login!')

def logout(request):
    request.session.flush()
    return redirect('/')

########################### Helper Methods
def genErrorMessages(request, results):
    for error in results['errors']:
        messages.error(request, error)