from scapy.all import *
import base64

FILE = "Exfil.pcap"
SOURCE_IP = '192.168.64.137'
DEST_IP = '138.197.108.176'
PROTO = ICMP

def filter_op(pkt):
	"""Filter operation for [PROTO] and [SRC_IP]"""
	return PROTO in pkt and pkt[IP].src == SOURCE_IP and pkt[IP].dst == DEST_IP


server_icmp = filter(filter_op, rdpcap(FILE))
data = ""

for packet in server_icmp:
	if packet[ICMP].type == 8:
		data += packet.load

with open('mystery.file', 'w') as f:
	f.write("".join(data))
