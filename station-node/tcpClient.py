import socket

def Main():
    host = '127.0.0.1' # host of the surver we are connecting to
    port = 5000 # port of server

    s = socket.socket() #create a new socket

    s.connect((host, port)) # connect to socket, wait until sucessful

    message = input("->") # if sucessful, ask for user input 
    while message != 'q':
        s.send(bytes(message, 'utf-8'))# send message to socket
        data = s.recv(1024) # wait for data to be recieved and save as data, data buffer = 1024
        print('RECIEVED_DATA' + str(data))
        message = input('-> ')# get user input again

    s.close() #close socket after q is typed

if __name__ == '__main__':
    Main()

