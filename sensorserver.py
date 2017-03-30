import time
import socket
import sys
import os
import operator
import threading

new_dict = {}

class Client(threading.Thread):
	lock = threading.Lock()

	def __init__(self,connection,client_address): 
		threading.Thread.__init__(self) 
		self.conn = connection
		self.clientaddress = client_address
 
	def run(self): 
		(ipofclient,port) = self.clientaddress
		
		while True:
			print("Received data from sensor ")
			data = self.conn.recv(10)
			print(str(data))
			filename = open("/home/jarvis/Documents/Docker/out.txt","r")
			line = filename.readline()
			line = line.split()

			if len(line) > 0:
				iptosend = line[0]
				print(iptosend)
				#iptosend = "172.31.84.177"
				porttosend = 10001
				computation_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				computation_address = (iptosend,porttosend)
				computation_sock.connect(computation_address)	
				computation_sock.send(data)
				print("hello")	

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("172.31.84.165",9997)
sock.bind(server_address)
sock.listen(10)

while True:
	print("Waiting for Sensor Data")
	connection,client_address = sock.accept()
	thread = Client(connection,client_address)		
	thread.start()