import socket

host = 'localhost'
port = 4021

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))
MAX_NUM_CLIENT = 1
sock.listen(MAX_NUM_CLIENT)
print(f'Server listen on port {port} ...')

#accept return connection and client address
conn, addr = sock.accept()
# print('Connection from address:',str(addr))

# conn.send(b'Hello how are you')#b''- convert to binary
# conn.send('bye...'.encode())# also convert to binary
# instead send text we will send file

BUFFER = 1024
file_name = conn.recv(BUFFER)
try:
    f = open(file_name,'rb')
    content = f.read()
    conn.send(content)
except Exception as e:
    print(e)
    conn.send(b'Problem to read a file - file does not exists?')
finally:
    f.close()

conn.close()
