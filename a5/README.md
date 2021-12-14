### CS 725/825 Computer Networks, IT 725 Network Technology  (Fall 2020) ###

# Assignment 5 #

*Name:* `Sandeep Kumar Paul`  
*Email:* `sp1430@wildcats.unh.edu`

### Program description ###

1. Required tools & platforms:
   - Linux
   - Node JS (Used version is v12.16.3)
   - Node JS modules
        - http
        - fs

2. You need to put the below files on **agate.cs.unh.edu** to serve it as a server machine.
 
   - myHTTPServer.js
   - index.html
   - my404.html

### Execution Steps ###

1. Execute below **server** node-JS file on **agate.cs.unh.edu** for create a server environment.
       
       [sp1430@rb2 ~]$ node myHTTPServer.js agate.cs.unh.edu 25013
       
   *[**Note:** the myHTTPServer.js file takes 2 command-line input values particularly in below order]*

        [sp1430@rb1 ~]$ node myHTTPServer.js <host-address> <port-number>

2. You should see an output on server console as shown below:

    ```HTTP Server is running on 'agate.cs.unh.edu' with port 25013.....```

3. Then, Open your browser(`Chrome`/`Safari`/`Mozilla`) from your laptop/desktop, in the address bar, type below mentioned http URL to access the 
`Offset calculator` webpage:

    - `http://agate.cs.unh.edu:25013`
     



**End Of File**