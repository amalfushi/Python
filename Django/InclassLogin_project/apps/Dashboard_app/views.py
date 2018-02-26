# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('This is a dashboard science!')

def dashboard(request):
    if 'first_name' not in request.session:
        return redirect('/')
    return render(request, 'Dashboard_app/dashboard.html')