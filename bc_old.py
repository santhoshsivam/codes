#Half Duplex Process Communication
from subprocess import Popen, STDOUT, PIPE
from threading import Thread

def getoutput(p):
	while p.poll() is None:
		print(p.stdout.readline().decode().strip())

p = Popen(['bc'], stdout=PIPE, stderr=STDOUT, stdin=PIPE)
t = Thread(target=getoutput, args=(p,))
t.start()

while p.poll() is None:
	inp = input("")
	inp = inp + "\n"
	p.stdin.write(inp.encode())
	p.stdin.flush()
