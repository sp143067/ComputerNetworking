### CS 725/825 Computer Networks, IT 725 Network Technology  (Fall 2020) ###

# Assignment 4 #

*Name:* `Sandeep Kumar Paul`  
*Email:* `sp1430@wildcats.unh.edu`

### Program description ###

1. Required tools & platforms:
   - Linux
   - Python (Used version is 3.8.3)
   - Python modules
        - socket
        - numpy
        - ssl
        - http.server
        - urllib.request
    
2. You need to put the below files on **rb1.cs.unh.edu** to serve it as a client machine.
 
   - clientTUH.py
   - clientTCPTLS.py
   - clientHTTPS.py

3. You need to put the below files on **rb2.cs.unh.edu** to serve it as a server machine.
 
   - serverTCP.py
   - serverUDP.py
   - serverHTTP.py
   - serverTCPTLS.py
   - serverHTTPS.py
   - index.html

### Execution Steps ###

1. Firstly, for **[TCP, UDP, HTTP]** protocols, 
     - Execute below **server** python files on **rb2.cs.unh.edu** on 3 different sessions / terminals simultaneously as shown in report PDF.
     
       - [sp1430@rb2 ~]$ python serverTCP.py 7001 10
       - [sp1430@rb2 ~]$ python serverUDP.py 7002 10
       - [sp1430@rb2 ~]$ python serverHTTP.py 7003
       
     - Then, execute below **client** python file on **rb1.cs.unh.edu** as shown in report PDF.
       - [sp1430@rb1 ~]$ python clientTUH.py 10.5.0.2 7001 7002 7003 10

*[**Note:** the clientTUH.py file takes 5 command-line input values particularly in below order]*

        [sp1430@rb1 ~]$ python clientTUH.py <link-address> <TCP-port> <UDP-port> <HTTP-port> <iteration-Value>


2. Secondly , for **[TCP-with-TLS]** protocol,

      - Execute below **server** python files on **rb2.cs.unh.edu** on 3 different sessions / terminals simultaneously as shown in report PDF.
        - [sp1430@rb2 ~]$ python serverTCPTLS.py 7001
    
      - Then, execute below **client** python file on **rb1.cs.unh.edu** as shown in report PDF.
        - [sp1430@rb1 ~]$ python clientTCPTLS.py 10.5.0.2 7001 10
3. Finally, for **[HTTPS]**  protocol,

      - Execute below **server** python files on **rb2.cs.unh.edu** on 3 different sessions / terminals simultaneously as shown in report PDF.
        - [sp1430@rb2 ~]$ python serverHTTPS.py 7001
    
      - Then, execute below **client** python file on **rb1.cs.unh.edu** as shown in report PDF.
        - [sp1430@rb1 ~]$ python clientHTTPS.py 10.5.0.2 7001 10




**End Of File**