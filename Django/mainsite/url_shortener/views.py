from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
from .models import TinyUrl
import random
import string


def index(request):
    return render(request, 'url_shortener/index.html', {})


def create(request):
    url = request.POST['url']
    code = rand_code()
    newUrl = TinyUrl(url=url, code=code)                   #new entry in the database
    newUrl.save()

    # redirect back to the index page
    return HttpResponse(code)


def rand_code():
    i = 0
    output = ""
    while i < 6:                                                      #shorten URL to 6 characters
        output += random.choice(string.ascii_lowercase)
        i += 1

    return output


def code_redirect(request, code1):
    tinyurl = get_object_or_404(TinyUrl, code=code1)
    url = tinyurl.url
    return HttpResponseRedirect('https://' + url)
