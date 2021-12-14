import sys
import socket
import time
import re
import numpy as np

HOST = "rb2.cs.unh.edu"
PORT = 5001

# TCP socket declaration
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

t3_t2_list = []
client_rtt = []
t1_for_offset = []
t2_for_offset = []

try:
    CLIENT_SOCKET.connect((HOST, PORT))
    # 'for' loop deployed to conduct multiple transaction between client and server
    for i in range(int(sys.argv[1])):
        t1 = time.time()
        CLIENT_SOCKET.sendall(b'Welcome to Client Network')

        t4 = time.time()
        server_data = CLIENT_SOCKET.recv(1024)

        # storing the t2 & t3 data which was send from server to client into a list
        t3_t2_list.append(server_data.decode("utf-8"))

        # calculating the (t4 - t1) on client side and then storing into a list as 'client_rtt'
        client_rtt.append((t4-t1))

        # list of times 't1' to use in offset calculation
        t1_for_offset.append(t1)

except ConnectionRefusedError:
    print("Please check the host and port connections")

CLIENT_SOCKET.close()

# 'server_rtt' list used to store the output of (t2 - t3)
server_rtt = []
for i in range(0,len(t3_t2_list)):
    t2_t3 = re.findall("\d+\.\d+",t3_t2_list[i])
    t2_for_offset.append(float(t2_t3[0]))
    server_rtt.append(float(t2_t3[1]) - float(t2_t3[0]))

# converting list items to NumPy array to perform arithmetic operations
server_RTT_array = np.asarray(server_rtt)
client_RTT_array = np.asarray(client_rtt)

# Calculating the round trip time (RTT) as (t4 - t1) - (t3 - t2)
RTT = client_RTT_array - server_RTT_array
print('Calculating RTT using the NumPy array.............../Done!')


# Calculating the Offset using below mentioned variables and storing it to 'OFFSET_array'
# t1 (from t1_for_offset)
# t2 (from t2_for_offset)
# RTT (from RTT)
OFFSET_array = []
for counter in range(0,len(t1_for_offset)):
    OFFSET_array.append((t1_for_offset[counter] + RTT[counter] / 2) - t2_for_offset[counter])

OFFSET_array = [abs(num) for num in OFFSET_array]
print('Calculating Clock Offset using RTT values.........../Done!')

# applying few estimation methods to get precise measurements of Clock Offset:
print('Minimum Of Clock Offset: {}'.format(np.min(np.asarray(OFFSET_array))))
print('Maximum Of Clock Offset: {}'.format(np.max(np.asarray(OFFSET_array))))
print('Mean Of Clock Offset: {}'.format(np.mean(np.asarray(OFFSET_array))))
print('Median Of Clock Offset: {}'.format(np.median(np.asarray(OFFSET_array))))
print('Standard Deviation Of Clock Offset: {}'.format(np.std(np.asarray(OFFSET_array))))
print('Variance Of Clock Offset: {}'.format(np.var(np.asarray(OFFSET_array))))