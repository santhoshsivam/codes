from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,'troeve_info/index.html')   
#print(__file__)
def carrer(request):
   return render(request,'troeve_info/carrer.html')


def contact(request):
   return render(request,'troeve_info/contact.html')


def about(request):
   return render(request,'troeve_info/about.html')