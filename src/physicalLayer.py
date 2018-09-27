import socket
from scapy.all import *
import optparse
import time
import datetime

parser = optparse.OptionParser()
parser.add_option('-s', dest='src_ip', default='')
parser.add_option('-d', dest='dest_ip', default='')
parser.add_option('-m', dest='method', default='recieve')
parser.add_option('-p', dest='port', type='int', default=12345)
(options, args) = parser.parse_args()
src_ip = options.src_ip
dest_ip = options.dest_ip
port = options.port
method = options.method

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((src_ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recievePacket():
    message = ''
    while True :
	    message, address = server_socket.recvfrom(512)
	    #return Ether(message)
	    f = open('main.txt','w')
	    f.write(message)
	    f.flush()
    return message

def sendPacket(packet, ip, port):
    message = str(packet)
    addr = (ip, port)
    client_socket.sendto(message, addr)

def main():
	if(method == "recieve") :
		recievePacket()
	else :
		sendPacket('Shashwat Banchhor' , dest_ip, port)

if __name__ == "__main__":
    main()
