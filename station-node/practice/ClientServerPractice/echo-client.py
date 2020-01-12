import socket

HOST = "127.0.0.1"  # The Server's Hostname / IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    userInput = input()
    while userInput != '':

        s.sendall(bytes(userInput, 'utf-8'))
        data = s.recv(1024)
        print('Reveived', repr(data))
        userInput = input()

print('Program finished')