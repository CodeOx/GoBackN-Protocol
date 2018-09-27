MAX_SEQ = 7

def between(a,b,c):
	if (((a<=b)&&(b<c)) || ((c<a) && (a<=b)) || ((b<c)&&(c<a))):
		return True
	else
		return False

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
		
def send_data(frame_nr,frame_expected,buffer):
	s = Frame(buffer[frame_nr],frame_nr,(frame_expected+MAX_SEQ)%(MAX_SEQ+1))
	# send to physical layer
	# start time


class Seq_nr(object):
	"""docstring for Seq_nr"""
	def __init__(self, arg):
		super(Seq_nr, self).__init__()
		self.arg = arg

	def inc(self):
		self.arg = (self.arg+1)%(MAX_SEQ+1)
		

next_frame_to_send = (-1)
ack_expected = (-1)
frame_expected = (-1)
r  = Frame(None,None,None)
packet_outbound = buffer[MAX_SEQ+1]
nbuffered = (-1)

enable_network_layer()
ack_expected = 0
frame_expected = 0
next_frame_to_send = 0
nbuffered  =0 





while True:

	if event < 4:
		if event == 0: # frame arrival
			r = get_from_phy_layer()
			if r.seq == frame_expected:
				to_network_layer(r.info)
				frame_expected += 1

			while (between(ack_expected,r.ack,next_frame_to_send)):
				nbuffered = nbuffered -1
				stop_timer()
				ack_expected+=1


		elif event==1: # cksum_err
			pass
		elif event==2: # timeout
			next_frame_to_send = ack_expected
			for i in xrange(1,nbuffered+1):
				send_data(next_frame_to_send,frame_expected,buffer)
				next_frame_to_send+= 1

		elif event ==3: # network_layer_ready
			# from net_layer
			new_packet  = buffer[next_frame_to_send]
			nbuffered = nbuffered +1
			send_data(next_frame_to_send,frame_expected,buffer)
			next_frame_to_send += 1 


	if nbuffered<MAX_SEQ :
		# enable net lay
	else
		# disable 
		