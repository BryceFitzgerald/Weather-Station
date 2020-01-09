import socket


class Server:
    def __init__(self, host, port):
        
        # create socket serverSocket
        self.serverSocket = socket.socket()
        # connection variable 
        self.incommingConnection = None

        # bind socket to server host and port variables
        self.host = host
        self.port = port
        self.connection = False

    
    def establishConnection(self):
        # bind host and port to socket with touple
        serverSocket.bind((host, port))

        # listen for connections (1 at a time)
        serverSocket.listen(1)
        self.connection = True

        # return a new socket connection c and address addr
        self.incommingConnection, self.addr = s.accept()
        
        # announce connection from address
        print("Connection from: " + str(addr))


    def closeConnection(self):
        if(self.incommingConnection == None):
        	self.connection == false
            return

        else:
            self.incommingConnection.close()
            self.connection = False

    def isConnected(self):
        return self.connection == True

    def submitMeasurement(self, measurement):
    	# to current connection, send data
        self.incommingConnection.send(bytes(str(measurement),'utf-8')) 

    # returns recieved command from client. buffer size is 1024 bytes
    def recieveCommand(self, executionObject):
        return incommingConnection.recv(1024)

        




