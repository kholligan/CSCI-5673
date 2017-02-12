# Client/server code adapted from 
# https://pymotw.com/2/socket/binary.html
import socket
import sys
import time
import struct

def time_request():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ("128.138.201.67", 8000)
	message = 'Sent request for server time'
	request = 'time'

	unpacker = struct.Struct('d d')

	try:
		# Send data
		print >>sys.stderr, '%s' % message
		send_time = time.time()
		sent = sock.sendto(request, server_address)
		# print >>sys.stderr, 'Send time is %f' % send_time

		# print >>sys.stderr, 'Waiting to receive...'
		data, server = sock.recvfrom(4096)
		rec_time = time.time()

		# print >>sys.stderr, 'Received response from server'
		# print >>sys.stderr, 'Receive time is %f' % rec_time
		
		unpacked_data = unpacker.unpack(data)
		# print >>sys.stderr, 'unpacked: %f, %f' % (unpacked_data[0], unpacked_data[1])


	finally:
		# print >>sys.stderr, 'Closing socket'
		sock.close()
		print("CSend: %f\tSRec: %f\tSSend: %f\tCRec: %f\t") % (send_time, unpacked_data[0], unpacked_data[1], rec_time)

for i in range(5):
	time_request()

