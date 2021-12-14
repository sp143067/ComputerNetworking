import socket
import sys

HOST = ''
PORT = int(sys.argv[1])

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((HOST, PORT))
print('My TCP server is listening on host {} & port {}.'.format(HOST, PORT))
SERVER_SOCKET.listen(1)
count = 0
while True:
    server_socket_object, client_addr = SERVER_SOCKET.accept()
    client_message = server_socket_object.recv(1024)
    if not client_message:
        break
    server_socket_object.sendall(bytes("Welcome to TCP server! Message has been received", encoding="utf-8"))
    count += 1
    #print("count = {}".format(count))
    if count == int(sys.argv[2]):
        break
    #print('\n')
