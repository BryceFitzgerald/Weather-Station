import socket

def Main():
    host = '192.168.56.1' # host of the surver we are connecting to
    port = 5000 # port of server

    s = socket.socket() #create a new socket

    s.connect((host, port)) # connect to socket, wait until sucessful

    message = input("->") # if sucessful, ask for user input 
   

    s.close() #close socket after q is typed

if __name__ == '__main__':
    Main()

