from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def run(request):
    file  = open('E://codes/htdocs/Project-sean/index.html')
    body  = file.read()
    return HttpResponse(body)