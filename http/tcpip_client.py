import socket

sock = socket.socket()

host = 'localhost'
port = 4000


sock.connect((host,port))

BUFFER = 1024
msg = sock.recv(BUFFER)

while(msg):
    print('Recieved ',msg.decode())
    msg = sock.recv(BUFFER)

sock.close()