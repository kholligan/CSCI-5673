# Client/server code adapted from
# https://pymotw.com/2/socket/binary.html
import socket
import sys
import time
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostbyname('0.0.0.0')
print host_name

server_address = (host_name, 8000)
print >>sys.stderr, 'Server started on %s port %s' % (server_address)
sock.bind(server_address)

while True:
	print >>sys.stderr, '\nWaiting to receive message...'
	data, address = sock.recvfrom(4096)
	# if data == "time":
	rec_time = time.time()

	print >>sys.stderr, 'Received %s bytes from %s' % (len(data), address)
	print >>sys.stderr, 'Message receive time %f' % rec_time

	if data:
		send_time = time.time()
		values = (rec_time, send_time)
		packer = struct.Struct('d d')
		packed_data = packer.pack(*values)
		sent = sock.sendto(packed_data, address)
		print >>sys.stderr, 'Sent %i bytes back to %s' % (sent, address)
		print >>sys.stderr, 'Message send time %f' % send_time
		# print("Send: %s, Rec: %s") % (time.ctime(send_time), time.ctime(rec_time))