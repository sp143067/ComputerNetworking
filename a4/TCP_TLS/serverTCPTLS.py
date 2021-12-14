import sys
import os
import socket
import ssl

BUFFER_SIZE = 1024
PORT = int(sys.argv[1])


# verifying if there is already a cert.pem file exist or not,
# If not, then using openssl command, cert.pem file is getting created.
# Python Doc reference: https://docs.python.org/3/library/ssl.html#self-signed-certificates
self_signed_cert = (os.path.join(os.getcwd() + "/cert.pem"))
if not os.path.exists(self_signed_cert):
    os.system("openssl req -new -x509 -out cert.pem -keyout cert.pem -days 365 -nodes --subj "
              "'/C=US/ST=NH/L=DURHAM/O=UNH/OU=UNHCS/CN=sp1430/emailAddress=sp1430@wildcats.unh.edu.com'")
    print("Successfully created the Self-Signed certificate using openSSL!")

# creating a new SSL context, where I am passing the version of the SSL protocol to use.
# for this assignment, I am using TLS protocol as ssl.PROTOCOL_TLS and
# Then, loading the certificate into the ssl-context using below load method.
# Python Doc reference: https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.load_cert_chain(certfile='cert.pem')

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_tls_address = ('', PORT)
serverSocket.bind(tcp_tls_address)
serverSocket.listen(1)
print('My TCP-TLS server is listening on port {}.'.format(PORT))

serverSocket_object, address = serverSocket.accept()

# Here, I am creating a SSL-socket using the existing TCP-socket.
# This SSL-socket is tied to it's certificate, setting & contexts.
with ssl_context.wrap_socket(serverSocket_object,server_side=True) as ssl_socket:
    while True:
        client_message = ssl_socket.recv(BUFFER_SIZE).decode()
        if not client_message:
            break
        ssl_socket.sendall(b'rb2: Welcome to CS825 class!')
        #print('recieved')
