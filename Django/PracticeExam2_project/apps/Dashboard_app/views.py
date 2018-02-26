# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from ..LoginReg3_app.models import User

# Create your views here.

def dashboard(request):
    if 'userID' not in request.session:
        return redirect('/')
    else:
        context = {
            'first_name' : User.objects.get(id=request.session['userID']).first_name,
            'last_name' : User.objects.get(id=request.session['userID']).first_name,
            'userID' : request.session['userID']
        }
        return render(request, "Dashboard_app/Dashboard.html", context)

def user(request, getUserID):
    if 'userID' not in request.session:
        return redirect('/')
    else:
        return render(request, 'Dashboard_app/user.html')