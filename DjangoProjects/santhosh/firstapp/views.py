from django.shortcuts import render,redirect
from .models import santhosh
from .models import signin as m_s
from faker import Faker
import random as r
from .forms import signin_form as sif
fake = Faker()
# Create your views here.
def again(request):
    fake = Faker()
    for i in range(100):
        sname = fake.name()
        sage = r.randint(1,80)
        sph =  r.randint(9000000000,9999999999)
        john =  santhosh.objects.create(name=sname,age=sage,phone=sph)


    send_to  = santhosh.objects.all()
    send_to.delete()
    
    return render(request, 'firstapp/index.html',context = {'send_to':send_to})


def signin_form(request):
    sf = sif()
    if request.method == "POST":
        form = sif(request.POST)
        if form.is_valid():
            uname = request.POST.get('uname')
            fname = request.POST.get('fname')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            P = m_s(uname=uname,fname=fname,password=password,phone=phone)
            P.save()
            return redirect('/form_index/')
        

    send_form = {'send':sf}
    return render(request, 'firstapp/forms.html',context=send_form)


def form_ind(request):
    send_to = m_s.objects.all()
    send = {'send_2':send_to}
    return render(request,'firstapp/forms.html',context=send)
