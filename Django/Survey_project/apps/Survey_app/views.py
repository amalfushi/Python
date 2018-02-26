# -*- coeding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def main(request):
    #setting default values for all fields 
    if not 'attempts' in request.session:
        request.session['attempts'] = 0
    if not 'your_name' in request.session:
        request.session['your_name'] = ''
    if not 'comment' in request.session:
        request.session['comment'] = ''
    if not 'dojo_location' in request.session:
        request.session['dojo_location'] = ''
    if not 'fav_language' in request.session:
        request.session['fav_language'] = ''

    #populates fields with values left over on failed validation(except the select inputs)
    return render(request, 'Survey_app/index.html', generateContext(request))

def process(request):
    #form validation
    errors = False
    #could add these to session['errors'] and check for it's lenghth instead of using errors variable
    if len(request.POST['your_name']) <1:
        #display error
        messages.error(request, 'Please Enter Your Name')
        errors = True

    if len(request.POST['dojo_location']) <1:
        messages.error(request, 'Please Choose A Location')
        errors = True

    if len(request.POST['fav_language']) <1:
        messages.error(request, 'Please Choose A Language')
        errors = True

    if len(request.POST['comment']) > 120:
        messages.error(request, 'Comments can only be 120 characters')
        errors = True

    #if there are errors, show some errors
    if errors:
        return redirect('/')
    else:
        request.session['attempts'] +=1
        request.session['your_name'] = request.POST['your_name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['fav_language'] = request.POST['fav_language']
        request.session['comment'] = request.POST['comment']
        
        return redirect('/results')

def results(request):
    return render(request, 'Survey_app/results.html', generateContext(request))

def go_back(request):
    request.session.pop('your_name')
    request.session.pop('comment')
    request.session.pop('dojo_location')
    request.session.pop('fav_language')
    return redirect('/')

def reset(request):
    request.session.pop('attempts')
    return redirect('/go_back')

def generateContext(request):

    context = {"name": request.session["your_name"], "comment": request.session["comment"], "dojo_location":request.session["dojo_location"], "fav_language":request.session["fav_language"], "attempts":request.session["attempts"]}
    print context
    return context