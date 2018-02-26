# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..LoginReg3_app import User

# Create your views here.
def dashboard(request):
    if 'userID' not in request.session:
        return redirect('/')
    else:
        context={
            'curUser' : User.objects.get(id=request.session['userID']),
            'otherUsers': User.objects.exclude(id=curUser.id),
        }
        return render(request, 'Pet_app/dashboard.html', context)

def user(request, userID):
    if userId not in request.session:
        return redirect('/')
    else:
        