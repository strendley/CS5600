#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:57:21 2019

@author: stbrb
"""
from socket import * #import socket module
import sys # In order to terminate the program


def main():
    
    #take in command line arguments
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    fname = sys.argv[3]

    #set the buffer size
    buffer_size = 4096
        
    #connect to the server
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.connect((server_host, server_port))
    
    #send the GET reuqest to the server
    serverSocket.sendall( ('GET /' + fname + ' HTTP/1.1 ').encode())
    #receive the servers data for the requested file
    messageData = serverSocket.recv(buffer_size)
    
    #close the connection to the server
    serverSocket.close()
    
    #print the contents of the message
    print(messageData)
        
if __name__ == '__main__':
    main()