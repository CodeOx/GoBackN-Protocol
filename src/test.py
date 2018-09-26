from scapy.all import *
send(IP(dst="1.2.3.4")/UDP(dport=123))