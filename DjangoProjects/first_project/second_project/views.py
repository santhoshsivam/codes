from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    file  = open('E:/codes/htdocs/Project-Sean/index.html','r')
    body = file.read()
    return HttpResponse(body)

def carrers(request):
    file  = open('E:/codes/htdocs/Project-Sean/carrer.html','r')
    body = file.read()
    return HttpResponse(body)

def contact(request):
    file  = open('E:/codes/htdocs/Project-Sean/contact.html','r')
    body = file.read()
    return HttpResponse(body)

def about(request):
    file  = open('E:/codes/htdocs/Project-Sean/about.html','r')
    body = file.read()
    return HttpResponse(body)
def styles(request):
    file  = open('E:/codes/htdocs/Project-Sean/css/styles.css','r')
    body = file.read()
    return HttpResponse(body)

def image(request):
    
    file  = open('E:/codes/htdocs/Project-Sean/images/','r')
    body = file.read()
    return HttpResponse(body)
