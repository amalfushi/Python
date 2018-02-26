# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import User, UserManager
from django.contrib import messages
import bcrypt

# Create your views here.

def test(request):
    return HttpResponse('This is a test!')

def main(request):
    return render(request, 'LogReg2_app/index.html')

def register(request):
    results = User.objects.validate_reg(request.POST)

    if results['errors']:
        for error in results['messages']:
            messages.error(request, error)
        return redirect('/')
    else:
        User.objects.createUser(request.POST)
        return HttpResponse('User Created')

def login(request):
    results = User.objects.validate_login(request.POST)

    if results['errors']:
        for error in results['messages']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['username'] = results['user'].username
        request.session['name'] = '{} {}'.format(results['user'].first_name, results['user'].last_name)
        request.session['email'] = results['user'].email
        return redirect('/dashboard')


def logout(request):
    request.session.flush()
    return redirect('/')
