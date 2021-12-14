import sys
import os
import ssl
from http import server

BUFFER_SIZE = 1024
HOST = ""
PORT = int(sys.argv[1])

# verifying if there is already a cert.pem file exist or not,
# If not, then using openssl command, cert.pem & pvt_key.pem file are getting created.
# Python Doc reference: https://docs.python.org/3/library/ssl.html#self-signed-certificates
self_signed_cert = (os.path.join(os.getcwd() + "/cert.pem"))
if not os.path.exists(self_signed_cert):
    os.system("openssl req -new -x509 -out cert.pem -keyout cert.pem -days 365 -nodes --subj "
              "'/C=US/ST=NH/L=DURHAM/O=UNH/OU=UNHCS/CN=sp1430/emailAddress=sp1430@wildcats.unh.edu.com'")
    print("Successfully created the Self-Signed certificate using openSSL!")

certFile = './cert.pem'

httpSocket = server.HTTPServer((HOST, PORT), server.SimpleHTTPRequestHandler)
# Wrap the socket with SSL
httpSocket.socket = ssl.wrap_socket(httpSocket.socket, certfile=certFile, server_side=True)
print('My HTTPS server is listening on port {}'.format(PORT))
httpSocket.serve_forever()
