import socket
import sys
import threading

def handleClient(conn,addr):
    print(f'criando thred para client {addr}')
    while True:
        
        data = conn.recv(1024)
        msg= str(data,'utf8')
        if '#close' in msg:
            conn.close()
            break
        print(f'[{addr}]: {msg}')
        conn.sendall(data)

# se '' vazio  recebe de qualquer endereço 
server_address=('',45654)
# socket.SOCK_STREAM =soket tcp
serverSoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSoket.bind(server_address)

serverSoket.listen(5) # cria lista de espera de 5 conexoes 

while True:
    # accept faz servidor esperar conexão
    print('aguardando conexões...')
    conn, addr = serverSoket.accept()
    print(f'conectado com o client{addr}')
    th= threading.Thread(target=handleClient,args=(conn,addr,))
    th.start()
