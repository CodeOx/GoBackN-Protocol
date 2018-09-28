import socket
from scapy.all import *
import time
import datetime

packet_recieved = False
message = ''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def start_network_layer(src_ip, port):
    server_socket.bind((src_ip, port))

def network_layer_ready():
    global packet_recieved
    if packet_recieved :
	packet_recieved = False
	return True
    return False

def from_network_layer():
    global message
    return message

def recieveFrame():
    global packet_recieved, message
    message = ''
    f2 = open('test1.txt', 'w')
    f2.write(str(datetime.datetime.now()))
    f2.flush()
    while True :
	    message, address = server_socket.recvfrom(512)
	    #return Ether(message)
	    
	    f = open('main.txt','w')
	    f.write(message)
	    f.flush()
	    packet_recieved = True
	    return
    return

def sendFrame(message, ip, port):
    f3 = open('test2.txt', 'w')
    f3.write(message)
    f3.flush()
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
	#go_back_n.data_link_enable()
	#if(method == "recieve") :
	#	t1 = threading.Thread(target=recievePacket, name='t1')
	#	t2 = threading.Thread(target=write, name='t2')
        #        t1.start()
	#	t2.start()
	#	t1.join()
	#	t2.join()
		#recievePacket()
	#else :
	#	time.sleep(5)
	#	sendPacket(str(datetime.datetime.now()) , dest_ip, port)

if __name__ == "__main__":
    main()
