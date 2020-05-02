import socket
import sys
import threading
import os 
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
           

        
            # head="HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Length: "+str(len(enviar))+"\r\n\r\n"
            arquivos = os.listdir() 
            print(arquivos)
            
                
            if msg[1][1:] in arquivos:
                
                conn.sendall(b'HTTP/1.1 200 OK\n')
                conn.sendall(b'Connection: close\n')
                conn.sendall(b'Content-Type: text/html\n')
                conn.sendall(b'\n')
                dado=open(msg[1][1:])
                dado='\n'.join(dado.readlines())
                conn.sendall(dado.encode())
                
            else:
                conn.sendall(b'HTTP/1.1 404 ERRO\n')
                conn.sendall(b'Connection: close\n')
                conn.sendall(b'Content-Type: text/html\n')
                conn.sendall(b'\n')
                conn.sendall(b'\n')
                conn.sendall(b'<html> <header> <title>ERRO 404</title>  </header>  <body > <H1>ERROR 404 PAGE NOT FOUND </H1> </body></html>')
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
