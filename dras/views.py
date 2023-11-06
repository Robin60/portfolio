#!/usr/bin/env python3


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    """View to index page"""
    template = loader.get_template('dras/index.html')
    return HttpResponse(template.render())

def info(request):
    """View to information center"""
    return render(request, 'dras.onrender.com')

def predict(request):
    """View to prediction interface"""
    return render(request, 'dras.onrender.com/Predictions')

def stats(request):
    """View to dras statistics"""
    return render(request, 'dras.onrender.com/Statistics')
