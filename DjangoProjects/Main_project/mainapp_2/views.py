from django.shortcuts import render,redirect
from .models import questions as questions
from .models import signin as signindb
from .models import fifth_standard as fifth_db
from .models import sixth_standard as sixth_db
from .models import seventh_standard as seventh_db
count = 1
correct  = 0
correct_list = []
Database =''
cookie = ''

def last_answer(request):
    global correct_list
    global Database
    get_db = []
    try:
        for e in correct_list: 
            g =Database.objects.get(Question_no = e)
            get_db.append(g)    
        return render(request, 'mainapp/answers.html', context={'varies':get_db})
    except:
        AttributeError()
        pass

def index(request):
        global count
        global correct
        global correct_list
        global cookie
        try:            
            if count > 10:
                    cookies = int(cookie)
                    time = 900 - cookies              
                    minutes = time //60
                    sec = time % 60
                    seconds  = time % 60
                    if ((time % 60) == 0):
                        seconds = str(seconds)
                        seconds = seconds + '0'
                    elif (sec > 0 and sec < 10):
                        seconds = str(seconds)
                        seconds = '0' + seconds
                    else:
                        seconds = str(seconds)
                                        
                    minutes = str(minutes)
                    send = minutes + ':' + seconds
                    return render(request, 'mainapp/select_standard.html', context={'finish':'finish','correct':correct , 'time':send})
            else:
            
                if request.method == "POST" and request.POST.get('submit') == "Submit":
                    value = request.POST.get('Question')
                    cookie = request.POST.get('cookie')
                    get_db = (Database.objects.get(Question_no=count))
                    match = get_db.Answer
                    vary = {'vary': get_db}
                    if match != value:
                        return render(request, 'mainapp/base.html', context={'answer_wrong':get_db,'vary':get_db})

                    else:              
                        correct = correct + 1
                        correct_list.append(count)
                        return render(request, 'mainapp/base.html', context={'answer_right': get_db, 'vary':get_db})
                    
                
                
                elif request.method == "POST" and request.POST.get('submit') == "Next":
                    cookie = request.POST.get('cookie')
                    if cookie == 0:
                        count = 11
                    else:
                        count = count + 1
                    
                    return  redirect('/index/')
                
                
                elif Database == '':    
                    return  redirect('/form/')

                else:
                    get_db = (Database.objects.get(Question_no = count))
                    
                    return render(request, 'mainapp/base.html',context =  {'vary': get_db, 'count': count})
        except:
            AttributeError()
            pass
     
def Login_page(request):
    return render(request,'mainapp/index.html')

def user_signin(request):
    global count
    global correct_list
    try:
        if request.method == "POST" and request.POST.get('submit') == "Login":
            if count > 1:
                count = 1
                correct_list = []
            reg_no = request.POST.get('uname')
            password = request.POST.get('pwd')
            groups = signindb.objects.filter( Register_number=reg_no,Password=password)
            if len(groups) == 1:  
                return render(request,'mainapp/select_standard.html') 
            else:
                failed = 'failed'
                fail_Ret = {'failed':failed}
                return render(request, 'mainapp/index.html',context = fail_Ret)
        

        elif request.method == "POST" and request.POST.get('submit') == "Signin":
            reg_no = request.POST.get('uname')
            password = request.POST.get('pswd')
            phoneNum = request.POST.get('phneno')
            eMail = request.POST.get('email')
            fullName = request.POST.get('fname')
            b = signindb.objects.filter( Register_number=reg_no)


            if len(b)<1:
                b = signindb.objects.create(Full_Name=fullName, Register_number=reg_no, Password=password, Mobile_number=phoneNum, Email_Id=eMail)
                success = 'success'
                sg_success = {'sg_success':success}
                return render(request,'mainapp/index.html',context = sg_success)
            else:
                failed = 'failed'
                sg_failed = {'failed':failed}
                return render(request,'mainapp/signin.html',context = sg_failed)
    except:
        AttributeError()
        pass


def signin_page(request):
    return render(request,'mainapp/signin.html')

def strt_test(request):
    global Database
    
    try:
        if request.method == "POST" and request.POST.get('submit') == "Submit":
            db = request.POST.get('Standard')
            if db == 'Five':
                Database = fifth_db
            elif db == 'Six':
                Database = sixth_db
            elif db == 'Seven':
                Database = seventh_db
            start = 'start'
            send = {'start_test':start}
            return render(request, 'mainapp/select_standard.html',context=send)
        elif request.method == "POST" and request.POST.get('submit') == "Start_Test":
            return redirect('/index/')
        elif request.method == "POST" and request.POST.get('submit') == "Continue.":
            return redirect('/form/')
    except:
        AttributeError()
        pass        
