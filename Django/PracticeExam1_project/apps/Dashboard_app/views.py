# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from ..LoginReg3_app.models import User
from models import Comment

# Create your views here.
def dashboard(request):
    if 'email' not in request.session or 'userID' not in request.session:
        return redirect('/')
    else:
        context= {
            'first_name': request.session['first_name'],
            'userID': request.session['userID'],
            'otherUsers': User.objects.exclude(id = request.session['userID']),
        }
        return render(request, 'Dashboard_app/Dashboard.html', context)

def user(request, getUserID):
    if 'email' not in request.session or 'userID' not in request.session:
        return redirect('/')
    else:
        curUser = User.objects.get(id=getUserID)
        context = {
            'getUser' :User.objects.get(id=getUserID),
            'comments' : curUser.recieved_comments.all(),
            'sender' : request.session['userID'],
            'recipient' : getUserID
        }
        return render(request, 'Dashboard_app/User.html', context)

def add(request):
    print request.POST
    results = Comment.objects.validateComment(request.POST)

    if results['status']:
        newComment = Comment.objects.createComment(request.POST)
        return redirect('/dashboard')