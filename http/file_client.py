import socket

sock = socket.socket()

host = 'localhost'
port = 4021


sock.connect((host,port))

BUFFER = 1024
# msg = sock.recv(BUFFER)

# while(msg):
#     print('Recieved ',msg.decode())
#     msg = sock.recv(BUFFER)

# we call for a file

file_name = input('Enter the file name you want: ')

sock.send(file_name.encode())

content = sock.recv(BUFFER)

print(content.decode())

sock.close()