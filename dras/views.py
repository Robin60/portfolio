#!/usr/bin/env python3


from django.shortcuts import render


def index(request):
    """View to index page"""

    return render(request, 'dras/index.html', {})
