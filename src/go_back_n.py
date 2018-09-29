import time
import optparse
import threading
import datetime
import physicalLayer
import networkLayer

MAX_SEQ = 3
PACKET_READY = False
EVENT = 0
BUFFER =[]
CLOCKS = [time.time() for i in range(MAX_SEQ)]
THRESHOLD = 20

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

class Frame(object):
	"""docstring for Frame"""
	def __init__(self, information,sequence,acknowledgement,checksum):
		super(Frame, self).__init__()
		self.info = information
		self.seq = sequence
		self.ack = acknowledgement
		self.checksum = checksum

class Packet(object):
	"""docstring for Packet"""
	def __init__(self, arg):
		super(Packet, self).__init__()
		self.arg = arg

def between(a,b,c):
	if (((a<=b)and(b<c)) or ((c<a) and (a<=b)) or ((b<c)and(c<a))):
		return True
	else:
		return False
		
def send_data(frame_nr,frame_expected,buffer):
	s = Frame(buffer[frame_nr],frame_nr,(frame_expected+MAX_SEQ)%(MAX_SEQ+1),len(buffer[frame_nr].arg))
	#Frame s = Frame(buffer[frame_nr],frame_nr,0)
	msg = make_msg_from_frame(s)	
	physicalLayer.sendFrame(msg,dest_ip, port)
	# send to physical layer
	# start time


class Seq_nr(object):
	"""docstring for Seq_nr"""
	def __init__(self, arg):
		super(Seq_nr, self).__init__()
		self.arg = arg

	def inc(self):
		self.arg = (self.arg+1)%(MAX_SEQ+1)

def make_msg_from_frame(frame):
    packet = frame.info
    #f3 = open('test2.txt', 'w')
    message =  str(frame.seq)+'/'+str(frame.ack)+'/'+str(packet.arg)+'/'+str(frame.checksum) 
    return message

def get_frame_from_msg(message):
    m = message.split('/')	
    recv_fr_seq = m[0]
    recv_fr_ack = m[1]
    message = m[2]
    checksum = m[3]
    recv_pkt = Packet(message)
    recv_fr = Frame(recv_pkt,int(recv_fr_seq),int(recv_fr_ack),int(checksum))
    return recv_fr

def check_time_out():
	global CLOCKS, THRESHOLD, MAX_SEQ
	t = time.time()	
		
	f = open('clock_log.txt','a')
	f.write('CLOCK_CHECK:   '+'\n')
	for i in range(MAX_SEQ):
		f.write(' '+str(i)+(': ')+str(CLOCKS[i])+'\n')
	f.flush()
	f.close()
	
	for i in range(MAX_SEQ):
		if (CLOCKS[i] != -1) :		
			if (t-CLOCKS[i] > THRESHOLD):
				return True
	return False

def check_sum_err(frame):
	message = frame.info.arg
	checksum = frame.checksum
	f = open('chk_sum_log.txt','a')
	f.write('CHK_SUM:  \n')
	f.write(' message: '  + message + ' checksum: '+str(checksum))
	f.flush()
	f.close()	
	if (checksum != len(message)):
		return True
	return False
	
	
def data_link_enable():
	global EVENT, BUFFER
	t0 = time.time()	
	next_frame_to_send = (-1)
	ack_expected = (-1)
	frame_expected = (-1)
	r  = Frame(None,None,None,None)
	#packet_outbound = buffer[MAX_SEQ+1]
	nbuffered = (-1)

	#enable_network_layer()
	#networkLayer.start_network_layer(src_ip, port)


	ack_expected = 0
	frame_expected = 0
	next_frame_to_send = 0
	nbuffered  =0 





	while (time.time()-t0 < 50):

		if EVENT < 4:
					
			if physicalLayer.physical_layer_ready(): # frame arrival
				M = physicalLayer.from_physical_layer()
 				r = get_frame_from_msg(str(M))
				#f11 = open(method + '_recieved_from_physical_layer.txt', 'a')
				#f11.write(M + '\n')
				#f11.flush()
				#f11.close()				
				if (check_sum_err(r)==False):					
					if r.seq == frame_expected:
						#write to file
						#f11 = open(method + '_sent_to_networkLayer.txt', 'a')
						#f11.write(r.info.arg + '\n')
						#f11.flush()
						#f11.close()
						#to_network_layer(r.info)
						networkLayer.pass_pkt(method + '_reached_network_layer.txt', r.info.arg)
						frame_expected = (frame_expected+ 1) % MAX_SEQ

					while (between(ack_expected,r.ack,next_frame_to_send)):
						nbuffered = (nbuffered -1)
						#stop_timer()
						CLOCKS[ack_expected] = -1					
						ack_expected = (ack_expected + 1) % MAX_SEQ


			#elif check_sum_err(): # cksum_err
			#	pass
			
			#elif False:
			elif check_time_out(): # timeout
				next_frame_to_send = ack_expected
				for i in xrange(1,nbuffered+1):
					send_data(next_frame_to_send,frame_expected,buffer)
					next_frame_to_send = (next_frame_to_send+ 1)%MAX_SEQ

			elif networkLayer.network_layer_ready(): # network_layer_ready
				# from net_layer
				f = open("entered_event3.txt",'a')
				
				new_packet = Packet(networkLayer.get_pkt(method+"_taken_from_net_layer.txt"))
				#new_packet = Packet('abcd') # send by net layer	
							
				BUFFER[next_frame_to_send] = (new_packet)
				f.write(BUFFER[next_frame_to_send].arg + '\n')
				f.close()
				#new_packet  = buffer[next_frame_to_send]
				CLOCKS[next_frame_to_send] = time.time()
				nbuffered = (nbuffered +1)
				send_data(next_frame_to_send,frame_expected,BUFFER)
				next_frame_to_send = (next_frame_to_send+ 1)%MAX_SEQ 
				EVENT = 0


		if nbuffered<MAX_SEQ :
			print  # enable net lay
		else:
			print
			 

BUFFER = [Packet('') for i in range(MAX_SEQ)]

physicalLayer.start_physical_layer(src_ip, port)
t1 = threading.Thread(target= physicalLayer.recieveFrame, name='t1')
t2 = threading.Thread(target = data_link_enable, name='t2')
t3 = threading.Thread(target = networkLayer.start_network_layer, name = 't3')

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
			
