import socket
from scapy.all import *
import time
import datetime

packet_recieved = False
message = ''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def start_physical_layer(src_ip, port):
    server_socket.bind((src_ip, port))

def physical_layer_ready():
    global packet_recieved
    if packet_recieved :
	packet_recieved = False
	return True
    return False

def from_physical_layer():
    global message
    return message

def recieveFrame():
    global packet_recieved, message
    message = ''
    while True :
	    message, address = server_socket.recvfrom(512)
	    #return Ether(message)
	    
	    f = open('recieved_from_other_host.txt','a')
	    f.write(message + '\n')
	    f.flush()
	    packet_recieved = True
	    return
    return

def sendFrame(message, ip, port):
    addr = (ip, port)
    client_socket.sendto(message, addr)

def write():
    fi = open('random.txt', 'w')
    for i in range(10) :
        fi.write(str(datetime.datetime.now()) + "\n")
	fi.flush()
	time.sleep(1)    

    

def main():
	print

if __name__ == "__main__":
    main()
