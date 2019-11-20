#!/usr/bin/env python3
'''
mimic ping with scapy
'''
from scapy.all import sr1,IP,ICMP

target = str(input("Enter target to ping: "))

ip = IP(dst=target)

response = sr1(ip/ICMP())

if response == None:
    print("No Response")
else:
    print("Target Responding")
