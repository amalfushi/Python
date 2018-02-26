# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from products import products

# Create your views here.

def main(request):
    try:
        request.session['products']
    except KeyError:
        request.session['products'] = products

    # print request.session['products']
    return render(request, 'Amadon_app/index.html')



def buy(request):
    #get item
    # print request.POST
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    
    try:
        request.session['item_count']
    except KeyError:
        request.session['item_count'] = 0

    for product in products:
        if product['id'] == int(request.POST['item_id']):
            try:
                request.session['subtotal']
            except KeyError:
                request.session['subtotal'] = 0

            request.session['subtotal'] = product['price']*int(request.POST['quantity'])
            request.session['total'] += request.session['subtotal']
            request.session['item_count'] += int(request.POST['quantity'])

    print request.session['item_count']
    print request.session['total']
    return redirect('/checkout')



def checkout(request):
    context ={
        'subtotal': request.session['subtotal'],
        'item_count': request.session['item_count'],
        'total': request.session['total'],
    }
    return render(request, 'Amadon_app/checkout.html', context)

def reset(request):
    request.session.pop('subtotal')
    request.session.pop('total')
    request.session.pop('item_count')

    return redirect('/')