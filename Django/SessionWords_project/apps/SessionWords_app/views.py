# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    try:
        request.session['words']
    except:
        request.session['words'] =[]

    # print request.session['words']
    return render(request, 'SessionWords_app/index.html')

def process(request):

    newWord={
        'color':request.POST['color'],
        'time': datetime.now().strftime("%H:%M %p, %B %d, %y"),
    }

    if request.POST['word'] == "":
        newWord['word'] = '?'
    else:
        newWord['word'] = request.POST['word']


    try:
        request.POST['bigoFont']
        newWord['bigoFont'] = 'Biggo'
    except:
        newWord['bigoFont'] =  'Smallo'

    print newWord
    temp_list = request.session['words']
    temp_list.append(newWord)
    request.session['words'] = temp_list

    print request.session['words']
    return redirect('/')

def reset(request):
    request.session.pop('words')
    return redirect('/')