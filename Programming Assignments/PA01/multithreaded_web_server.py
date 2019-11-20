#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:59:08 2019

@author: stbrb
"""

from socket import * #import socket module
import sys # In order to terminate the program
import threading #In order to support multithreading

buffer_size = 1024

class WebThread(threading.Thread):
    def __init__(self, con, addr):
        threading.Thread.__init__(self)
        self.connectionSocket = con
        self.address = addr
        
    def run(self):
        #while True:
        try:
            message = self.connectionSocket.recv(buffer_size)
            
            filename = message.split()[1]
            f = open(filename[1:])
            outputData = f.read()
            f.close()
            
            #Send one HTTP header line into socket          
            self.connectionSocket.send("\nHTTP/1.1 200 OK \n\n".encode())
            #print("reached 1")
            #send the content of the requested file to the client
            for i in range(0, len(outputData)):
                self.connectionSocket.send(outputData[i].encode())
            
            #print("reached 2")    
            self.connectionSocket.send("\r\n".encode())       
            #self.connectionSocket.close()
            #print("reached 3")
            
            
        except IOError:
            
            #print('Connection ERROR')
            #send resposnse message for file not found
            self.connectionSocket.send("\nHTTP/1.1 404 Not Found \n\n".encode())
            self.connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            #print("reached 4")
            #Close the client socket
            self.connectionSocket.close()
            
def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #Prepare the server socket
    serverPort=9876
    serverSocket.bind(('',serverPort))
    
    #initialize threads list
    threads=[]
    
    while True:
        #start listening
        serverSocket.listen(5)

        #Establish the connection
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        #print("accepted socket addr")
        #create a new thread
        newThread = WebThread(connectionSocket, addr)
        #print("created new thread")
        #append it to the list of threads
        threads.append(newThread)
        #start the thread
        newThread.run()               
        #print("started thread")
        #for thread in threads:
         #   thread.join()
    #close the server socket
    
    #print("appended thread")
    #print("joined threads") 
    
    serverSocket.close()
    #print("closed server socket")
    #terminate the program after sending corresponding data
    sys.exit() 
        
            

if __name__ == '__main__':
    main()
    
    
        
        
        
        
                