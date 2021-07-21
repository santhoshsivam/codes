from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def santhosh(request):
    file = open("C:/xamppe/htdocs/Project-sean/index.html")
    body = file.read()
    return HttpResponse(body)