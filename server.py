import socket
import sys
import threading
import os 
import time
import html_parser
import post_parser
# ngrok http 45654
def head(path, response):
    header='HTTP/1.1 '+ response +'\r\n'
    # header+='Connection: close\r\n'
    # header+='Content-Encoding: UTF-8\r\n'
    header+='Content-Length: ' + str(os.path.getsize(path)) + '\r\n'
    header+='Expires: -1\r\n'
    header+='Last-Modified: ' + str(time.ctime(os.path.getmtime(path))) + '\r\n'
    header+='Content-Type: text/'+path.split('.')[1]+'; charset=UTF-8\r\n'
    header+='\r\n'
    return header

def handleClient(conn,addr):
    #print(f'criando thred para client {addr}')
    
        
    aux = conn.recv(1024)
    data = aux
    print(len(aux))
    conn.settimeout(1.0)
    while len(aux) == 1024:
        try:
            aux = conn.recv(1024)
            data += aux
        except socket.timeout:
            break


    msg= str(data,'utf8')

    # print(f'[{addr}]: {msg}')
    # print(msg)
    awn=html_parser.process_message('svr',msg)
    # print(awn)
    if awn: 
        if os.path.exists(awn['path']): #verifica de o arquivo existe

            if awn['command'] =='GET' :
                a=open(awn['path'])
                dado=head(awn['path'],'200 OK')+('\n'.join(a.readlines()))
                conn.sendall(dado.encode())
                a.close()
            # head="HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Length: "+str(len(enviar))+"\r\n\r\n"
            elif awn['command']=='HEAD':
                conn.sendall(head(awn['path']).encode())
            elif awn['command'] == 'POST':
                print('POST')
                print(awn)
                post_parser.process_post('post_index.txt', awn['msg'])
                a = open(awn['path'])
                dado = head(awn['path'], '204 OK') + ('\n'.join(a.readlines()))
                conn.sendall(dado.encode())
                a.close()
        else:
            conn.sendall(b'HTTP/1.1 404 ERRO\n')
            conn.sendall(b'Connection: close\n')
            conn.sendall(b'Content-Type: text/html\n')
            conn.sendall(b'\n')
            conn.sendall(b'<html> <header> <title>ERRO 404</title>  </header>  <body > <H1>ERROR 404 PAGE NOT FOUND </H1> </body></html>')
            
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
