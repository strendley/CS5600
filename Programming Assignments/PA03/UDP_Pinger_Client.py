#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write this code!
"""
import socket
from socket import AF_INET, SOCK_DGRAM
import time
buffer_size = 1024
host = '127.0.0.1'
port = 12000

def main():
    
    clientSocket = socket.socket(AF_INET, SOCK_DGRAM) #create the client socket
    clientSocket.settimeout(1) #set the timeout to 1 second
    seqNum = 1 #keep track of sequence numbers
    rtt = [] #store rtt values in a list
    
    print('')
    print('Pinging ' + host + ' on port ' + str(port))
    print('')
    
    while seqNum <= 10:
        startTime = time.time() #get the start time
        message = str(seqNum)
        clientSocket.sendto(message.encode(),(host,port)) #send message to the server
        
        try:
            message, address = clientSocket.recvfrom(buffer_size)
            rTime = (time.time() - startTime) #rtt time
            rtt.append(rTime)
            print('PING ' + str(seqNum) + ': RTT Time = ' + str(rTime) + ' sec')
        except socket.timeout:
            print('PING ' + str(seqNum) + ': TIMED OUT')
        
        seqNum +=1 #increment the seqNum to the next packet
        
    if(seqNum > 10): #10 packets have been received
        avg = sum(rtt,0.0)/len(rtt)
        lossRate = str((10-len(rtt))*10) 
        
        print('')
        print('Ping Stats')
        print('Max RTT = ' + str(max(rtt)) + ' sec')
        print('Min RTT = ' + str(min(rtt)) + ' sec')
        print('Avg RTT = ' + str(avg) + ' sec')
        print('Packet Loss Rate = ' + lossRate + '%')
        clientSocket.close()

if __name__ == '__main__':
    main()
