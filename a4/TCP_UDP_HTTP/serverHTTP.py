import sys
import http.server
from socketserver import TCPServer

# SimpleHTTPRequestHandler class helps in serve current directory as a server with HTTP protocol
handlerHTTP = http.server.SimpleHTTPRequestHandler
PORT = int(sys.argv[1])

# 'TCPServer' helps define a TCP protocol for uninterrupted streams of data between the client and server
# 'server_forever': it's a loop where the socket serves for the defined protocol
with TCPServer(('', PORT), handlerHTTP) as httpSocket:
    print("HTTP server is listening on port: {} ".format(PORT))
    httpSocket.serve_forever()