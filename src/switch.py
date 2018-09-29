import time
import random
from random import randint

DATA_ERROR_PROBABILITY= 0
ACK_ERROR_PROBABILITY = 0
DROP_PROBABILITY = 0

def data_error(message):
	m = message.split('/')
	data = m[2]
	n = random.uniform(0,1)
	if (n <= DATA_ERROR_PROBABILITY) :
		data = data[:len(data)-1]
	m[2] = data
	return '/'.join(m)	

def ack_error(message):
	m = message.split('/')
	ack = m[1]
	n = random.uniform(0,1)
	if (n <= ACK_ERROR_PROBABILITY) :
		ack = int(ack) + 1
	m[1] = str(ack)
	return '/'.join(m)

def drop_packet():
	n = random.uniform(0,1)
	if (n <= DROP_PROBABILITY) :
		return True
	return False
