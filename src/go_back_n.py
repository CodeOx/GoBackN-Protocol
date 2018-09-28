import time
import optparse
import threading
import datetime
import physicalLayer
from physicalLayer import Frame,Packet

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





def between(a,b,c):
	if (((a<=b)and(b<c)) or ((c<a) and (a<=b)) or ((b<c)and(c<a))):
		return True
	else:
		return False
		
def send_data(frame_nr,frame_expected,buffer):
	s = Frame(buffer[frame_nr],frame_nr,(frame_expected+MAX_SEQ)%(MAX_SEQ+1))
	physicalLayer.sendPacket(buffer[frame_nr],dest_ip, port)
	# send to physical layer
	# start time


class Seq_nr(object):
	"""docstring for Seq_nr"""
	def __init__(self, arg):
		super(Seq_nr, self).__init__()
		self.arg = arg

	def inc(self):
		self.arg = (self.arg+1)%(MAX_SEQ+1)
		
def data_link_enable():
	global EVENT
	t0 = time.time()	
	next_frame_to_send = (-1)
	ack_expected = (-1)
	frame_expected = (-1)
	r  = Frame(None,None,None)
	#packet_outbound = buffer[MAX_SEQ+1]
	nbuffered = (-1)

	#enable_network_layer()
	ack_expected = 0
	frame_expected = 0
	next_frame_to_send = 0
	nbuffered  =0 





	while (time.time()-t0 < 50):

		if EVENT < 4:
			if physicalLayer.physical_layer_ready(): # frame arrival
				r = physicalLayer.from_physical_layer()
				f = open('abc.txt', 'w')
				f.write(r)
				f.flush()
				#if r.seq == frame_expected:
					#write to file
					#to_network_layer(r.info)
					#frame_expected += 1

				#while (between(ack_expected,r.ack,next_frame_to_send)):
				#	nbuffered = nbuffered -1
					#stop_timer()
				#	ack_expected+=1


			elif EVENT==1: # cksum_err
				pass
			elif EVENT==2: # timeout
				next_frame_to_send = ack_expected
				for i in xrange(1,nbuffered+1):
					send_data(next_frame_to_send,frame_expected,buffer)
					next_frame_to_send+= 1

			elif EVENT ==3: # network_layer_ready
				# from net_layer
				#new_packet = 'abcd'
				new_packet = Packet('abcd')				
				BUFFER.append(new_packet)
				#new_packet  = buffer[next_frame_to_send]
				nbuffered = nbuffered +1
				send_data(next_frame_to_send,frame_expected,BUFFER)
				next_frame_to_send += 1 
				EVENT = 0


		if nbuffered<MAX_SEQ :
			print
			# enable net lay
		else:
			print
			# disable 


physicalLayer.start_physical_layer(src_ip, port)
t1 = threading.Thread(target= physicalLayer.recievePacket, name='t1')
t2 = threading.Thread(target = data_link_enable, name='t2')

if method=='send' : 	
	EVENT = 3

t1.start()
t2.start()
t1.join()
t2.join()

			
