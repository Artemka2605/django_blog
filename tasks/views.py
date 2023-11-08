from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):

    return HttpResponse('Hello')

