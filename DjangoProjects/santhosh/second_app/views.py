from django.shortcuts import render
from second_app.models import baby
from second_app.models import santhosh
import time
from .models import baby
from .models import mistorminor
# Create your views here.
def hey(request):
    stud_name = ['santhosh', 'sangeetha', 'Baby', 'Bby boy']
    stud_age = [35,35,8,5]
    stud_phone = [9952565717, 9597901409, 9546546464, 8754446768]

    for i in range(0, len(stud_name)):
        mistorminor.objects.create(name=stud_name[i],age=stud_age[i],phone=stud_phone[i])
    
    qu = mistorminor.objects.all()
    vary = {'vary':qu}
    return render(request,'secondapp/time.html',context=vary)
