from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def crawl(request):
    return HttpResponse('test')
