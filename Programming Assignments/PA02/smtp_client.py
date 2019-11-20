#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sept 25 10:34:11 2019

@author: stbrb
"""

from socket import *
import ssl;

def main():
    msg = "\r\n I love computer networks!"
    endmsg = "\r\n.\r\n"
    
    server = 'gmail-smtp-in.l.google.com'
    serverPort = 25
    senderEmail = "strendley094@gmail.com"
    receiverEmail = "stbrb@mst.edu"
    
    #create the mail server
    mailserver = (server, serverPort)
    
    #Create a client socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    
    #get the message from the client socket
    recv = clientSocket.recv(1024).decode()
    #print the message
    print(recv)
    
    #if the message does not contain the 220 reply code, notify user
    if recv[:3] != '220':
        print('220 reply not received from server.')
      
    # Send HELO command and print server response
    heloCommand = 'EHLO smtp.google.com\r\n'
    clientSocket.send(heloCommand.encode())
    
    #get the message from the client socket
    recv1 = clientSocket.recv(1024).decode()
    
    #print the message
    print(recv1)
    
    #if the message does not contain the 250 reply code, notify user
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    
    #Send the FLS command before the MAILFROM command
    TLSCommand = 'STARTTLS\r\n'
    clientSocket.send(TLSCommand.encode())
    
    recvTLS = clientSocket.recv(1024).decode()
    print(recvTLS)
    
    if recvTLS[:3] != '220':
        print('220 reply not received from server.')
    
    clientSocket = ssl.wrap_socket(clientSocket)
    
    # Send MAIL FROM command and print server response.
    fromCommand = 'MAIL FROM: ' + senderEmail + '\r\n'
    clientSocket.send(fromCommand.encode())
    
    #get the message from the client socket
    recv2 = clientSocket.recv(1024).decode()
    
    #print the message
    print(recv2)
    
    # Send RCPT TO command and print server response.
    rcptCommand = 'RCPT TO: ' + receiverEmail + '\r\n'
    clientSocket.send(rcptCommand.encode())
    
    #get the message from the clientSocket
    recv3 = clientSocket.recv(1024).decode()
    
    #print the message
    print(recv3)
    
    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    
    #get the message from the clientSocket
    recv4 = clientSocket.recv(1024).decode()
    
    #print the message
    print(recv4)
    
    # Send message data.
    clientSocket.send(msg.encode())
    
    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print(recv5)
    
    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6)
    
    
if __name__ == '__main__':
    main()