from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))
