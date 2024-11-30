from django.http import HttpRequest, HttpResponse
from django.template import Template, context
from django.template.loader import get_template
from django.shortcuts import render

def home(request):
    return render(request, 'market/home.html', {})