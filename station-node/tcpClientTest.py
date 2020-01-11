import socket
import time

def Main():
    host = '192.168.56.1' # host of the surver we are connecting to
    port = 5000 # port of server

    s = socket.socket() #create a new socket

    s.connect((host, port)) # connect to socket, wait until sucessful

   
    data = s.recv(2048)
    startTime = time.time()
    while data != "SERVER_COMMAND:EXIT" or (time.time() - startTime <= 5.0):
        print("Data Recieved" + str(data) + str(time.time()))
        data = s.recv(2048)
    s.close() #close socket after q is typed
    print("PROGRAM COMPLEATED")

if __name__ == '__main__':
    Main()

