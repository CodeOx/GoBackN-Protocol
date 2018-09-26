import socket
from scapy.all import *
import optparse

parser = optparse.OptionParser()
parser.add_option('-i_src', dest='src_ip', default='')
parser.add_option('-i_dest', dest='dest_ip', default='')
parser.add_option('-p', dest='port', type='int', default=12345)
(options, args) = parser.parse_args()
src_ip = options.src_ip
dest_ip = options.dest_ip
port = options.port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((src_ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recievePacket():
    message, address = server_socket.recvfrom(1024)
    #return Ether(message)
    return message

def sendPacket(packet, ip, port):
    message = str(packet)
    addr = (ip, port)
    client_socket.sendto(message, addr)

def main():
	method = input()
	if(method == "recieve") :
		print recievePacket()
	else :
		sendPacket('abcd' , dest_ip, port)

if __name__ == "__main__":
    main()