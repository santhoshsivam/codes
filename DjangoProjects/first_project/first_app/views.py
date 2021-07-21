from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def run(request):
    file = open ('C:/xamppe/htdocs/Project-sean/index.html','r')
    body=file.read()   
    return HttpResponse(body)
     
