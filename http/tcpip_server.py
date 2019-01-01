import socket

host = 'localhost'
port = 4000

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))
MAX_NUM_CLIENT = 1
sock.listen(MAX_NUM_CLIENT)
print(f'Server listen on port {port} ...')

#accept return connection and client address
conn, addr = sock.accept()
print('Connection from address:',str(addr))

conn.send(b'Hello how are you')#b''- convert to binary
conn.send('bye...'.encode())# also convert to binary

conn.close()
