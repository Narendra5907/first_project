from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<marquee><h1 color=blue>srujana tinnava ra</h1></marquee>')

def Nare(request):
    return HttpResponse('<marquee><h1>Nare is goodboy</h1></marquee>')

