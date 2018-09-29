import socket
from scapy.all import *
import time
import datetime

OBTAINED_FROM_DATALINK = []
TO_SEND_TO_DATA_LINK = ['The','sun','rises','in','the','east','and','sets','in','the','west']
count = -1

NETWORK_LAYER_READY = False

def start_network_layer():
    global NETWORK_LAYER_READY,TO_SEND_TO_DATA_LINK, count
    while count < len(TO_SEND_TO_DATA_LINK) :
	time.sleep(1)
	#f = open("started_network_layer.txt",'a')
	#f.close()
	NETWORK_LAYER_READY = True	

def network_layer_ready():
    global NETWORK_LAYER_READY
    f = open('network_layer_ready.txt', 'a')
    f.write(str(datetime.datetime.now())+ "   Count:  "+str(count) + '\n')
    f.flush()
    if NETWORK_LAYER_READY :
	f.write('True: ' + str(datetime.datetime.now()) + '\n')
	f.flush()
	f.close()
	NETWORK_LAYER_READY = False
	return True
    f.close()
    return False

def get_pkt(filename):
	global count,TO_SEND_TO_DATA_LINK
	f = open('log.txt','a')
	f.write('PACKET SENT	:	' + TO_SEND_TO_DATA_LINK[count+1] + '	:	' + str(datetime.datetime.now()) + '\n')
	f.flush()	
	f.close()
	count = count+1
	return TO_SEND_TO_DATA_LINK[count]

def pass_pkt(filename, message):
	global OBTAINED_FROM_DATALINK
	OBTAINED_FROM_DATALINK.append(message)
	f = open(filename, 'a')
    	f.write(message + '\n')
    	f.flush()
	f.close()
	f = open('log.txt', 'a')
	f.write('PACKET RECEIVED	:	' + message + '	:	' + str(datetime.datetime.now()) + '\n')
	f.flush()
	f.close()



def main():
	print

if __name__ == "__main__":
    main()
