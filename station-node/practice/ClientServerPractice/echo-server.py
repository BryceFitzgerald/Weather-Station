# Diagram : https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg

""" Echo Server:
        Server simply capitalizes what the client has sent. Server then resends message 
        Client


"""

import socket

HOST = '127.0.0.1'    # standard loopback interface address (localhost)
PORT = 65432          # Port listen on (non- privileged ports are > 1023)

# socket.socket() supports the context manager type, so you can use it in a with statment
# context managers are objects with special __enter__() and __exit__() functions.
# the with statment guarentees that the __enter__() statment will be called to set up the block of code
# it also guarentees that the __exit__() statment will be called ath te time of exit (no matter how the block is exited)
# the with statment is the prefered way to handel a task with a well-defined setup and teardown



# AF_INET is the adress family. SOCK_STREAM is the socket type for tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
    s.bind((HOST, PORT)) # bind associates a socket with a host and port number
    s.listen() # listen enables a server to accept() connections: Creates a listening socket
    conn, addr = s.accept() # socket() blocks and waits for an incomming connection
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # temporarily suspends the application until a connection is received
            if not data:
                break
            print(data)
            data = data.upper()
            conn.sendall(data)