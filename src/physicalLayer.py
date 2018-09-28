import socket
from scapy.all import *
import time
import datetime

class Frame(object):
	"""docstring for Frame"""
	def __init__(self, information,sequence,acknowledgement):
		super(Frame, self).__init__()
		self.info = information
		self.seq = sequence
		self.ack = acknowledgement

class Packet(object):
	"""docstring for Packet"""
	def __init__(self, arg):
		super(Packet, self).__init__()
		self.arg = arg


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

def recievePacket():
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

def sendPacket(packet, ip, port):
    f3 = open('test2.txt', 'w')
    f3.write(str(packet.arg))
    f3.flush()
    message = str(packet.arg)
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
