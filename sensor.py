import time
import socket
import sys
import psutil

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("172.31.84.165", 9997)
#print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	while(True):
	    message = psutil.cpu_percent()
	    message = str(message)
	    print(message)
	    '''print >> sys.stderr, 'sending "%s"' % message'''
	    sock.sendall(message.encode())
	    time.sleep(1)

finally:
    #print >> sys.stderr, 'closing socket'
    sock.close()
