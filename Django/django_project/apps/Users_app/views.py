# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def main(request):
    return HttpResponse('Placeholder to later display all the list of users')

def new(request):
    return redirect('/register')

def register(request):
    return HttpResponse('Placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to login')