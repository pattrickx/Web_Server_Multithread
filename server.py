import socket
import sys
import threading

def handleClient(conn,addr):
    print(f'criando thred para client {addr}')
    while True:
        
        data = conn.recv(1024)
        msg= str(data,'utf8')
        # if '#close' in msg:
        #     conn.close()
        #    
        print(f'[{addr}]: {msg}')
        if 'GET' in msg:
            msg=msg.split(" ")
            print('#############################')
            print()
            print(f'pegando informação {msg[1][1:]}')
            dado=open(msg[1][1:]+'.html','rb')
            enviar=dado.read()
            head="HTTP/1.1 200 OK\nConnection: close\nContent-Length: "+str(len(enviar))+"\nContent-Type: text/html\n"
            
            enviar=head.encode()+enviar
            print(enviar)
            conn.sendall(enviar)
            dado.close
        break
    conn.close()    
        # conn.sendall(data)

# se '' vazio  recebe de qualquer endereço 
client_address=('',45654)
# socket.SOCK_STREAM =soket tcp
serverSoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSoket.bind(client_address)

serverSoket.listen(5) # cria lista de espera de 5 conexoes 

while True:
    # accept faz servidor esperar conexão
    print('aguardando conexões...')
    conn, addr = serverSoket.accept()
    print(f'conectado com o client{addr}')
    th= threading.Thread(target=handleClient,args=(conn,addr,))
    th.start()
