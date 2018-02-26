# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import Course, CourseManager
from django.contrib.messages import error

# Create your views here.
def test(request):
    return HttpResponse('This is a test!')

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'Course_app/index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)

    if len(errors) > 0:
        for error in errors:
            error(request, error)
    else:
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')

def confirm(request, courseID):
    context = {
        'course': Course.objects.get(id=courseID)
    }
    return render(request, 'Course_app/confirm.html', context)

def delete(request, courseID):
    delCourse = Course.objects.get(id=courseID)
    delCourse.delete()
    return redirect('/')
