#!/usr/bin/env python3

# Derived from:
# https://gist.github.com/pklaus/856268

import socket
import struct
import random
import time
import select
import math
import sys

ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname('icmp')


def checksum(source_string):
    """
    Given the bytes array, it calculates the checksum and returns it.
    """
    # I'm not too confident that this is right but testing seems to
    # suggest that it gives the same answers as in_cksum in ping.c.
    sum = 0
    count_to = (len(source_string) / 2) * 2
    count = 0
    while count < count_to:
        this_val = (source_string[count + 1])*256 + (source_string[count])
        sum = sum + this_val
        sum = sum & 0xffffffff
        count = count + 2
    if count_to < len(source_string):
        sum = sum + (source_string[len(source_string) - 1])
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    # Swap bytes. Bugger me if I know why.
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def create_packet(id):
    """
    Create a new echo request packet based on the given "id".
    """
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, 0, id, 1)
    data = ''
    # Calculate the checksum on the data and the dummy header.
    my_checksum = checksum(header + data.encode('utf-8'))
    # Now that we have the right checksum, we put that in. It's just easier
    # to make up a new header than to stuff it into the dummy.
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), id, 1)
    return header + data.encode('utf-8')

"""
Receive the ping from the socket.
Returns 0 if a timeout occurs.
Returns (src_ip_address, ping_time_milliseconds) if successful.
"""
def receive_ping(my_socket, packet_id, time_sent, timeout):
    time_left = timeout
    while True:
        started_select = time.time()
        ready = select.select([my_socket], [], [], time_left)
        how_long_in_select = time.time() - started_select
        if ready[0] == []: # Timeout
            return 0
        time_received = time.time()
        rec_packet, addr = my_socket.recvfrom(1024)
        # The last 8 bytes are the header of the packet we sent to the server
        icmp_header = rec_packet[-8:]
        type, code, checksum, p_id, sequence = struct.unpack(
                'bbHHh', icmp_header)
        if p_id == packet_id:
            total_time_ms = (time_received - time_sent) * 1000
            # Round to 3 decimal places:
            total_time_ms = math.ceil(total_time_ms * 1000) / 1000
            return (addr[0], total_time_ms)
        time_left -= time_received - time_sent
        if time_left <= 0:
            return 0

"""
Sends an ICMP ping to the given host, and gets the response for that ping.
It sets the TTL in the IP header of the packet to the given value.
Returns 0 if a timeout occurs.
Returns (src_ip_address, ping_time_milliseconds) if successful.
"""
def echo_one(host, ttl):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
    my_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    # Maximum for an unsigned short int c object counts to 65535 so
    # we have to sure that our packet id is not greater than that.
    packet_id = int(random.random() * 65535)
    packet = create_packet(packet_id)
    while packet:
        # The icmp protocol does not use a port, but the function
        # below expects it, so we just give it a dummy port.
        sent = my_socket.sendto(packet, (host, 1))
        packet = packet[sent:]

    ping_res = receive_ping(my_socket, packet_id, time.time(), timeout)
    my_socket.close()
    return ping_res

"""
Given the host and a TTL value, it sends 3 pings.
Formats a nice user friendly string.
Returns (user_friendly_string, destination_reached).
destination_reached is True if the IP address who replied matches the host,
and False otherwise.
"""
def echo_three(host, ttl):
    try1 = echo_one(host, ttl)
    try2 = echo_one(host, ttl)
    try3 = echo_one(host, ttl)

    if try1 == 0:
        try1str = '*'
    else:
        try1str = try1[0] + ' - ' + str(try1[1]) + ' ms'
    if try2 == 0:
        try2str = '*'
    else:
        try2str = try2[0] + ' - ' + str(try2[1]) + ' ms'
    if try3 == 0:
        try3str = '*'
    else:
        try3str = try3[0] + ' - ' + str(try3[1]) + ' ms'

    final_string = try1str + ', ' + try2str + ', ' + try3str
    final_string = str(ttl) + '  ' + final_string

    if try1 == 0:
        destination_reached = False
    else:
        destination_reached = try1[0] == host

    return (final_string, destination_reached)

# -------------------------- #
# Main execution starts here #
# -------------------------- #

if len(sys.argv) <= 1:
    print('Bad usage. Provide a hostname.')
    sys.exit(1)

dest_addr = sys.argv[1]
# Domain name to IP address conversion:
host = socket.gethostbyname(dest_addr)
timeout = 3
max_tries = 30

print('myTraceRoute to ' + dest_addr + ' (' + host + '), ' + str(max_tries) +
      ' hops max.')

try:
    # Loop until we hit the maximum number of hops, or until we reach the
    # final destination host:
    for x in range(1, max_tries+1):
        (line, destination_reached) = echo_three(host, x)
        print(line)
        if destination_reached:
            break
except Exception as err:
    print(err)
except KeyboardInterrupt as err:
    print(err)
