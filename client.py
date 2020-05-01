import socket
import sys
import time
import threading

def recvFromServer(conn):
    while True:
        data = conn.recv(1024)
        msg= str(data,'utf8')
        print('[SERVER]: ',msg)
        if 'close' in msg:
            break
        
    clientSoket.close()



server_address=('localhost',45654)

clientSoket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSoket.connect(server_address)

th = threading.Thread(target=recvFromServer, args=(clientSoket,))
th.start()

# clientSoket.sendall(b'Hello World!')
# data =clientSoket.recv(1024)
recvDataLen=0
while True:
    msg = input('')
    if'#close' in msg:
        clientSoket.sendall(msg.encode('utf8'))
        break
    clientSoket.sendall(msg.encode('utf8'))

clientSoket.close()
