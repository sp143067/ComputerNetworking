import socket
import time
import numpy as np
import sys
import requests

BUFFER_SIZE = 1024
inet = sys.argv[1]
tcpPORT = int(sys.argv[2])
udpPORT = int(sys.argv[3])
httpPORT = sys.argv[4]
iteration = int(sys.argv[5])

tcpRTT = []
udpRTT = []
httpRTT = []


def processProtocol(host, protocol):
    """
    :param host: any one of these IPv4 address "10.5.0.2", "10.5.1.2", "10.5.2.2",
                 which passed via command line argument
    :param protocol: it will take these protocols respectively in the defined list [TCP, UDP, HTTP]
    :return: a list corresponding to above protocol which contain 'iteration'
             number of items.
    """
    if protocol == "TCP":
        tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpPort = tcpPORT
        t1 = time.time()
        tcp_client_socket.connect((host, tcpPort))
        tcp_client_socket.sendall(b'Hi RB2, I know you are doing well irrespective of Covid Pandemic!')
        tcp_client_socket.recv(BUFFER_SIZE)
        tcp_client_socket.close()
        t2 = time.time()
        RTT = (t2 - t1) * 1000
        tcpRTT.append(RTT)
        return tcpRTT

    if protocol == "UDP":
        udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpPort = udpPORT
        t1 = time.time()
        udp_client_socket.connect((host, udpPort))
        udp_client_socket.sendall(b'Hi RB2, I know you are doing well irrespective of Covid Pandemic!')
        udp_client_socket.recv(BUFFER_SIZE)
        udp_client_socket.close()
        t2 = time.time()
        RTT = (t2 - t1) * 1000
        udpRTT.append(RTT)
        return udpRTT

    if protocol == "HTTP":
        t1 = time.time()
        URL = 'http://' + host + ':' + httpPORT + '/index.html'
        httpResponse = requests.get(URL)
        t2 = time.time()
        RTT = (t2 - t1) * 1000
        httpRTT.append(RTT)
        return httpRTT


protocolList = ["TCP", "UDP", "HTTP"]

# rb2 interfaces: enp5s0f0, enp5s0f1, enp5s0f2
# ipV4: "10.5.0.2", "10.5.1.2", "10.5.2.2"
# ipv6: fd50:4abe:b885:500::2, fd50:4abe:b885:501::2, fd50:4abe:b885:502::2

print("Connected to Interface/Link: {}".format(inet))
print('\n')

for p in protocolList:
    # print("Protocol: {}".format(p))
    if p == 'TCP':
        for count in range(0, iteration):
            tcpRTT = processProtocol(inet, p)
        print('Mean of TCP RTT: {} milliseconds'.format(np.mean(np.asarray(tcpRTT))))

    if p == 'UDP':
        for count in range(0, iteration):
            udpRTT = processProtocol(inet, p)
        print('Mean of UDP RTT: {} milliseconds'.format(np.mean(np.asarray(udpRTT))))

    if p == 'HTTP':
        for count in range(0, iteration):
            httpRTT = processProtocol(inet, p)
        print('Mean of HTTP RTT: {} milliseconds'.format(np.mean(np.asarray(httpRTT))))
