import sys
import os
import time
import numpy as np
import ssl
import urllib.request

HOST = sys.argv[1]
httpsPORT = sys.argv[2]

httpsRTT = []

# verifying if there is already a cert.pem file exist or not,
# If not, then using openssl command, cert.pem & pvt_key.pem file are getting created.
# Python Doc reference: https://docs.python.org/3/library/ssl.html#self-signed-certificates
self_signed_cert = (os.path.join(os.getcwd() + "/cert.pem"))
if not os.path.exists(self_signed_cert):
    os.system("openssl req -new -x509 -out cert.pem -keyout cert.pem -days 365 -nodes --subj "
              "'/C=US/ST=NH/L=DURHAM/O=UNH/OU=UNHCS/CN=sp1430/emailAddress=sp1430@wildcats.unh.edu.com'")
    print("Successfully created the Self-Signed certificate using openSSL!")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ssl_context.load_cert_chain(certfile='cert.pem')
for i in range(0, int(sys.argv[3])):
    t1 = time.time()
    URL = 'https://' + HOST + ':' + httpsPORT + '/index.html'
    # passing the above defined ssl_context to the urllib.request method
    # to request a secure connection
    httpsResponse = urllib.request.urlopen(URL, context=ssl_context)
    t2 = time.time()
    #    print(httpsResponse.read())
    RTT = (t2 - t1) * 1000
    httpsRTT.append(RTT)

print("Connected to Interface/Link: {}".format(HOST))
# print('RTT: {}'.format(httpsRTT))
print('\n')
print('Mean RTT of {} is: {} milliseconds'.format(HOST, np.mean(np.asarray(httpsRTT))))
print('Median RTT of {} is: {} milliseconds'.format(HOST, np.median(np.asarray(httpsRTT))))
print('Standard Deviation RTT of {} is: {} milliseconds'.format(HOST, np.std(np.asarray(httpsRTT))))
print('Variance RTT of {} is: {} milliseconds'.format(HOST, np.var(np.asarray(httpsRTT))))
print('Minimum RTT of {} is: {} milliseconds'.format(HOST, np.min(np.asarray(httpsRTT))))
print('Maximum RTT of {} is: {} milliseconds'.format(HOST, np.max(np.asarray(httpsRTT))))
