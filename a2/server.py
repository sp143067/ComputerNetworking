import socket
import json
import time



HOST = 'rb2.cs.unh.edu'
PORT = 5001
json_list= []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SERVER_SOCKET:
    SERVER_SOCKET.bind((HOST, PORT))
    print('My server is listening on host {} & port {}.'.format(HOST, PORT))
    SERVER_SOCKET.listen(1)
    server_socket_object, client_addr = SERVER_SOCKET.accept()
    with server_socket_object:
        while True:
            t2 = time.time()
            client_message = server_socket_object.recv(1024)
            if not client_message:
                break
#            server_rtt = {"t2": t2,"t3": time.time()}
            server_rtt_json = json.dumps({"t2": t2,"t3": time.time()})
            server_socket_object.sendall(bytes(server_rtt_json, encoding="utf-8"))
