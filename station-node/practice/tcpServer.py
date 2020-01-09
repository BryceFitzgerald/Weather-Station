import socket

def Main():
    host = '192.168.1.14'  #Set Host as this machine (127.0.0.1)
    port = 5000 # sets port as 5000

    s = socket.socket() # Create Socket object
    s.bind((host, port))  # bind host and socket to a port
   

    s.listen(1)  # begin listeining, only for one connection at a time

    c, addr = s.accept()  #returns a new socket connection c, and address addr

    print("Connection from: " +str(addr)) # print address to terminal

    #### Now try to talk to the incoming connection
    while True:  # Forever
        data = c.recv(1024) #bytes recieved is saved as variable data. maximum buffer size is 1024 bytes
        if not data:  # if no data is recieved, the connection will be broken
            break
        
        # Print data from the user
        print("CONNECTED_USER: " + str(addr)+"\nRECIEVED_BYTES: "+str(data))

        data = str(data).upper() # change data to upper case
        print("SENT_BYTES: " + str(data)) # announce data to be sent

        c.send(bytes(data,'utf-8')) # to current connection, send data
    
    c.close()   # After not data protocall is run, close socket


if __name__== '__main__':
    Main()



