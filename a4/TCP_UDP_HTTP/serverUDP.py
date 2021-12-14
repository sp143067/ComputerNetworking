import socket
import sys

HOST = ''
PORT = int(sys.argv[1])

# SOCK_DGRAM: it helped in performing UDP protocol functionality
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER_SOCKET.bind((HOST, PORT))
print('My UDP server is listening on host {} & port {}.'.format(HOST, PORT))
count = 0
while True:
    client_message, address = SERVER_SOCKET.recvfrom(1024)
    if not client_message:
        SERVER_SOCKET.close()
    SERVER_SOCKET.sendto(bytes("Welcome to UDP server! Message has been received", encoding="utf-8"), address)
    count += 1
    #print("count = {}".format(count))
    if count == int(sys.argv[2]):
        break
    #print('\n')