import time
import optparse
import threading
import datetime
import physicalLayer
import networkLayer

MAX_SEQ = 7
PACKET_READY = False
EVENT = 0
BUFFER =[]

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

def between(a,b,c):
	if (((a<=b)and(b<c)) or ((c<a) and (a<=b)) or ((b<c)and(c<a))):
		return True
	else:
		return False
		
def send_data(frame_nr,frame_expected,buffer):
	s = Frame(buffer[frame_nr],frame_nr,(frame_expected+MAX_SEQ)%(MAX_SEQ+1))
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
    message =  str(frame.seq)+str(frame.ack)+str(packet.arg) 
    return message

def get_frame_from_msg(message):	
    recv_fr_seq = message[0]
    recv_fr_ack = message[1]
    message = message[2:len(message)-1]
    recv_pkt = Packet(message)
    recv_fr = Frame(recv_pkt,int(recv_fr_seq),int(recv_fr_ack))
    return recv_fr
	
def data_link_enable():
	global EVENT, BUFFER
	t0 = time.time()	
	next_frame_to_send = (-1)
	ack_expected = (-1)
	frame_expected = (-1)
	r  = Frame(None,None,None)
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
				f11 = open(method + '_recieved_from_physical_layer.txt', 'a')
				f11.write(M + '\n')
				f11.flush()
				if r.seq == frame_expected:
					#write to file
					f11 = open(method + '_sent_to_networkLayer.txt', 'a')
					f11.write(M + '\n')
					f11.flush()
					#to_network_layer(r.info)
					networkLayer.pass_pkt(method + '_reached_network_layer.txt', M)
					frame_expected += 1

				while (between(ack_expected,r.ack,next_frame_to_send)):
					nbuffered = nbuffered -1
					#stop_timer()
					ack_expected+=1


			elif EVENT==1: # cksum_err
				pass
			elif EVENT==2: # timeout
				next_frame_to_send = ack_expected
				for i in xrange(1,nbuffered+1):
					send_data(next_frame_to_send,frame_expected,buffer)
					next_frame_to_send+= 1

			elif networkLayer.network_layer_ready(): # network_layer_ready
				# from net_layer
				new_packet = Packet(networkLayer.get_pkt())
				#new_packet = Packet('abcd') # send by net layer	
							
				BUFFER.append(new_packet)
				#new_packet  = buffer[next_frame_to_send]
				nbuffered = nbuffered +1
				send_data(next_frame_to_send,frame_expected,BUFFER)
				next_frame_to_send += 1 
				EVENT = 0


		if nbuffered<MAX_SEQ :
			print  # enable net lay
		else:
			print
			 


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
			
