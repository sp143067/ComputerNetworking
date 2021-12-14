### CS 725/825 Computer Networks, IT 725 Network Technology  (Fall 2020) ###

# Assignment 3 #

*Name:* Sandeep Kumar Paul  
*Email:* `sp1430@wildcats.unh.edu`

### Program description ###

1. Required platform:
   > Linux
   
  and tools-libraries:
   > Python (Used version is 3.8.3)
   > socket Python-library
  

2. You need to put the below two files in a linux platform. Here I used 'agate.cs.unh.edu' Linux server. 
   > a3.sh
   > a3.py


3. To perform a hardcoded SMTP conversation using Netcat tool & Expect script; run below command on agate.cs.unh.edu

	[sp1430@agate ~]$ ./a3.sh


4. To perform a SMTP conversation using Python Socket library and user-specified inputs of sender, receiver, Subject & Body of the message; run below command:
	
	[sp1430@agate ~]$ python a3.py

then, on terminal the program will prompt for inputs; as shown in below sample:
	
	Enter the Sender mail id in correctly formated: sandeeppaul1205@gmail.com
	Enter a valid Recipient mail id: sp1430@wildcats.unh.edu
	Enter the Subject of your email: Test Email
	Enter the Message you want to send: Hello, How are you?

[Note: for step-4, make sure you are providing a valid recipient mail-id, so that you can log into your mail account and verify the SMTP message!]

#######################  End Of File  ########################