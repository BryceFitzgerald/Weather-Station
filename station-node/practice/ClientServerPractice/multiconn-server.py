import selectors
sel = selectors.DefaultSelector()
#...

# This portion of the porgram sets up the listening socket
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create listening socket with from ipv4 family and is tcp socket
lsock.bind((host, port)) # bind socket to host and port
lsock.listen() # listen for incoming traffic
print('Listening on', (host, port)) #announce litening 
lsock.setblocking(False) # calls made to this program will not 
sel.register(lsock, selectors.EVENT_READ, data=None) # registers the socekt to be monitored with eht sel.select() for the event your intersting en. for teh listening socekt, we want read events: selectors.EVENT_READ

# data is ued to store whateever arbitrary data you'd like along with teh socekt. It's returend when select returns. we'll use data to keep trak o what has been sent and recieved on the socket

# EVENT LOOP LMAO

while True:
    events = sel.select(timeout=None) # blocks until there are socekts ready for IO, returns a list of tuples, one for each socket.key is a selectorkey namedtulpe 
                                      # that contains a fileobject attribute.key.fileobj is the socket object and mask is an event mask of the operations that are ready
    for key, mask in events:
        # if the key data is none, then we know that its from the listening socket and must be accept().
        if key.data is None:
        	# we call our own accept() function as accept_wrapper()to get the new socekt object and register it with the selector
            accept_wrapper(key.fileobj)
        else: # if key data is not none, we know it's a client socket that's alredy been accepted and we will need to be serviced
              # service_connection is called and passed key and mask, which containse everythin we need to peratate on the socekt
            service_connection(key, mask)


# DEFINE ACCEPT WRAPER FUNCTION

def accept_wrapper(sock): # accept wrapper function, passed socket
    conn, addr = scok.accept() # socket should be ready to read, so accept normally
    print("accepted connection from ",addr) # announce acception
    conn.setblocking(False) #set socket to nonblocking mode
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'') # create an object to hold the data we want included along with the socket using teh class types.SimpleNamespace
    events = selectors.EVENT_READ | selectors.EVENT_WRITE # since we want to know when teh clinet connectio is ready for reading and writingm, both of those events are set using the following
    sel.register(conn, events, data=data) # the events mask, socket, and data objects are passed to sel.register


# DEFINE SERVICE CONNECTION FUNCTION
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ: # if socket is ready for reading, then mask & selctors.Event_read is true and sock.recv() is called
        recv_data = sock.recv(1024) # should be ready to read
        if recv_data:
            data.outb += recv_data # any data that is read is appended to data.outb so it can be sent ready
        else:    # if no data is received and the client has closed this socket, the server should to. don't forget to first call sel.unregister() so it's no longer monitored by select()
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print('echoing', repr(data.outb), "to", data.addr)
                sent = sock.send(data.outb) # any data received was stored in data.outb and is ready to be mirrored. this data is echoed to the clinet using sock.send()
                dat.outb = data.outb[sent:] # the bytes sent are removed from the send buffer



                ## PROGRAM FINISHED, next time, write multi-connection client

                https://realpython.com/python-sockets/