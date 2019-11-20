#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:59:08 2019

@author: stbrb
"""

from socket import * #import socket module
import sys # In order to terminate the program           
        
def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    #Prepare the server socket
    serverPort=6789
    serverSocket.bind(('localhost',serverPort))
    serverSocket.listen(1)
    buffer_size = 1024
    
    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        
        try:
            message = connectionSocket.recv(buffer_size)
            filename = message.split()[1]
            f = open(filename[1:])
            outputData = f.read()
            
            #Send one HTTP header line into socket          
            connectionSocket.send("\nHTTP/1.1 200 OK \n\n".encode())
            
            #send the content of the requested file to the client
            for i in range(0, len(outputData)):
                connectionSocket.send(outputData[i].encode())
                
            connectionSocket.send("\r\n".encode())       
            #connectionSocket.close()
            
        except IOError:
            
            #send resposnse message for file not found
            connectionSocket.send("\nHTTP/1.1 404 Not Found \n\n".encode())
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            
            #Close the client socket
            #connectionSocket.close()
        
        #close the server socket
        serverSocket.close()
        
        #terminate the program after sending corresponding data
        sys.exit()
        
            

if __name__ == '__main__':
    main()
    
    
        
        
        
        
                