# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import User
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.flush()
    return redirect('/')

def test(request):
    return HttpResponse('This is for science!')

def main(request):    
    return render(request, 'InclassLogin_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        User.objects.createUser(request.POST)
        messages.success(request, "Your user has been created. Please login.")
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    print results
    if results['status'] == True:
        for error in results['errors']:
            print error
            messages.error(request, error)
            return redirect('/')
    else:
        request.session['first_name'] = results['user'].first_name
        request.session['id'] = results['user'].id
        request.session['email'] = results['user'].email

    return redirect('/dashboard')