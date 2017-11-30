from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'url_shortener/index.html', {})


def create(request):
    return render(request, 'url_shortener', {})

