# Client/server code adapted from 
# https://pymotw.com/2/socket/binary.html
import socket
import sys
import time
import struct

def time_request():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ("ENTER IP ADDRESS HERE", 8000)
	message = 'Sent request for server time'
	request = 'time'

	unpacker = struct.Struct('d d')

	try:
		# Send data
		print >>sys.stderr, '%s' % message
		send_time = time.time()
		sent = sock.sendto(request, server_address)
		
		data, server = sock.recvfrom(4096)
		rec_time = time.time()
		
		unpacked_data = unpacker.unpack(data)

	finally:
		# print >>sys.stderr, 'Closing socket'
		sock.close()
		print("CSend: %f\tSRec: %f\tSSend: %f\tCRec: %f\t") % (send_time, unpacked_data[0], unpacked_data[1], rec_time)

for i in range(5):
	time_request()

