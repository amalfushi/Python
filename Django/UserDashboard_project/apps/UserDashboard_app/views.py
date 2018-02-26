# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('This is for science!')

def index(request):
    return render(request, 'UserDashboard_app/index.html')