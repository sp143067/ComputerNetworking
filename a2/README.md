### CS 725/825 Computer Networks, IT 725 Network Technology  (Fall 2020) ###

# Assignment 2 #

*Name:* Sandeep Kumar Paul  
*Email:* `sp1430@wildcats.unh.edu`

### Program description ###

1. Required platform:
   > Linux
   
  and libraries:
   > python (Used version is 3.8.3)
   > numpy (for array formation)
  

2. Make sure, you have put below:
   > 'server.py' file on the host rb2.cs.unh.edu &
   > 'client.py' file on the host rb1.cs.unh.edu


3. Then run below command on 'rb2.cs.unh.edu' to establish a server connection:
	
	[sp1430@rb2 ~]$ python server.py


4. Once you see the prompt as 'My server is listening on host rb2.cs.unh.edu & port 5001', then log into 'rb1.cs.unh.edu 'in another session and execute below command to run .client.py' file:
	
	[sp1430@rb1 ~]$ python client.py 30

[Note: In the above command at step-4; you see an command-line-argument as 30, which is an interger value representing the number of times the handshake communication or transaction you want to perform]

#######################  End Of File  ########################