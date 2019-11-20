#!/usr/bin/env python3
'''
mimic traceroute with scapy
'''
#traceroute.py
 

from scapy.all import *

hostname = str(input("Enter hostname to traceroute: "))

print("traceroute to",hostname,", 30 hops max, 60 byte packets")
for i in range(1,31):
    packet = IP(dst=hostname,ttl=i) / ICMP()
    reply = sr1(packet, verbose=0,timeout=1)
    if reply == None:
        print(i, " * * *")
    else:
        print(i, reply.src)