import socket
from scapy.all import *
import time
import datetime

OBTAINED_FROM_DATALINK = []
TO_SEND_TO_DATA_LINK = ['a','e','i','o','u']
count = -1

NETWORK_LAYER_READY = False

def start_network_layer():
    global NETWORK_LAYER_READY,TO_SEND_TO_DATA_LINK, count
    while count < len(TO_SEND_TO_DATA_LINK) :
	time.sleep(3)
	NETWORK_LAYER_READY = True
	

def network_layer_ready():
    global NETWORK_LAYER_READY
    f = open('netowrk_layer_ready.txt', 'w')
    if NETWORK_LAYER_READY :
	f.write(str(datetime.datetime.now()) + '\n')
	f.flush()
	NETWORK_LAYER_READY = False
	return True
    return False

def get_pkt():
	global count,TO_SEND_TO_DATA_LINK
	count = count+1
	return TO_SEND_TO_DATA_LINK[count]

def pass_pkt(filename, message):
	global OBTAINED_FROM_DATALINK
	OBTAINED_FROM_DATALINK.append(message)
	f3 = open(filename, 'a')
    	f3.write(message + '\n')
    	f3.flush()

def write():
    fi = open('random_network.txt', 'w')
    for i in range(10) :
        fi.write(str(datetime.datetime.now()) + "\n")
	fi.flush()
	time.sleep(1)    

def main():
	print

if __name__ == "__main__":
    main()
