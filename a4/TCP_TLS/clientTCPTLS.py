import sys
import socket
import ssl
import time
import numpy as np
import os

BUFFER_SIZE = 1024
HOST = sys.argv[1]
PORT = int(sys.argv[2])

tcptlsRTT = []

# verifying if there is already a cert.pem file exist or not,
# If not, then using openssl command, cert.pem file is getting created.
# Python Doc reference: https://docs.python.org/3/library/ssl.html#self-signed-certificates
self_signed_cert = (os.path.join(os.getcwd() + "/cert.pem"))
if not os.path.exists(self_signed_cert):
    os.system("openssl req -new -x509 -out cert.pem -keyout cert.pem -days 365 -nodes --subj "
              "'/C=US/ST=NH/L=DURHAM/O=UNH/OU=UNHCS/CN=sp1430/emailAddress=sp1430@wildcats.unh.edu.com'")
    print("Successfully created the Self-Signed certificate using openSSL!")

# Defining a TCP socket with address type IPv4
tcp_tls_address = (HOST, PORT)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# creating a new SSL context, where I am passing the version of the SSL protocol to use.
# for this assignment, I am using TLS protocol as ssl.PROTOCOL_TLS and
# Then, loading the certificate into the ssl-context using below load method.
# Python Doc reference: https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.load_cert_chain(certfile='cert.pem')

# Here, I am creating a SSL-socket using the existing TCP-socket.
# This SSL-socket is binded to it's certificate, setting & contexts.
ssl_socket = ssl_context.wrap_socket(clientSocket, server_side=False, server_hostname=HOST)
try:
    ssl_socket.connect(tcp_tls_address)
    print("Connected to Interface/Link: {}".format(HOST))
    for i in range(0, int(sys.argv[3])):
        t1 = time.time()
        ssl_socket.sendall(b'Hi rb2')
        server_message = ssl_socket.read(BUFFER_SIZE).decode('utf-8')
        t2 = time.time()
        RTT = (t2 - t1) * 1000
        tcptlsRTT.append(RTT)
finally:
    ssl_socket.close()

# print('RTT of {} is: {}'.format(HOST, tcptlsRTT))
print('\n')
print('Mean RTT of {} is: {}'.format(HOST, np.mean(np.asarray(tcptlsRTT))))
print('Median RTT of {} is: {}'.format(HOST, np.median(np.asarray(tcptlsRTT))))
print('Standard Deviation RTT of {} is: {}'.format(HOST, np.std(np.asarray(tcptlsRTT))))
print('Variance RTT of {} is: {}'.format(HOST, np.var(np.asarray(tcptlsRTT))))
print('Minimum RTT of {} is: {}'.format(HOST, np.min(np.asarray(tcptlsRTT))))
print('Maximum RTT of {} is: {}'.format(HOST, np.max(np.asarray(tcptlsRTT))))
