import socket 
import time
import psutil
 
host = '172.31.84.165' 
port = 9994	
BUFFER_SIZE = 10 
#MESSAGE = psutil.cpu_percent()
MESSAGE = 1.0
MESSAGE = str(MESSAGE)
MESSAGE = MESSAGE[2:-1]
print MESSAGE
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
 
while True: 
	MESSAGE = psutil.cpu_percent()
	print MESSAGE
	tcpClientA.send(str(MESSAGE))
	time.sleep(1)     
 
tcpClientA.close() 