import socket
from scapy.all import *
import time
import datetime
import switch

packet_recieved = False
message = []

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
    M = message
    message = []
    return M

def recieveFrame(filename):
    global packet_recieved, message
    while True :
	    m, address = server_socket.recvfrom(512)
	    message.append(m)
	    f = open(filename,'a')
	    f.write(m + str(datetime.datetime.now()) +  '\n')
	    f.flush()
	    f.close()
	    packet_recieved = True
    return

def sendFrame(filename, message, ip, port):
    f = open(filename, 'a')
    message = switch.data_error(message)
    message = switch.ack_error(message)
    if (not switch.drop_packet()):
	    f.write(message + str(datetime.datetime.now())+ '\n')
	    f.flush()
	    addr = (ip, port)
	    client_socket.sendto(message, addr)
    f.close()

def write():
    fi = open('random.txt', 'w')
    for i in range(10) :
        fi.write(str(datetime.datetime.now()) + "\n")
	fi.flush()
	time.sleep(1)
    fi.close()    

    

def main():
	print

if __name__ == "__main__":
    main()
