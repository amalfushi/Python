# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('This is a test!')

def dashboard(request):
    if 'email' not in request.session:
        return redirect('/')
    else:
        return render(request, 'Dashboard/dashboard.html')