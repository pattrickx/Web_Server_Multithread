import socket
import sys
import threading
import os 
import time
import html_parser
# ngrok http 45654
def head(path, response):
    header='HTTP/1.1 '+ response +'\r\n'
    header+='Connection: close\r\n'
    # header+='Content-Encoding: UTF-8\r\n'
    header+='Content-Length: ' + str(os.path.getsize(path)) + '\r\n'
    header+='Expires: -1\r\n'
    header+='Last-Modified: ' + str(time.ctime(os.path.getmtime(path))) + '\r\n'
    header+='Content-Type: text/'+path.split('.')[1]+'; charset=UTF-8\r\n'
    header+='\r\n'
    return header

def handleClient(conn,addr):
    #print(f'criando thred para client {addr}')
    while True:
        
        data = conn.recv(1024)
        msg= str(data,'utf8')

        # print(f'[{addr}]: {msg}')
        awn=html_parser.process_message('svr',msg)
        # print(awn)
        # print()
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
                print(awn['msg'])
                arquivo = open("svr/chat/chat.txt")
                lista = ''.join(arquivo.readlines())
                arquivo.close()
                arquivo = open("svr/chat/chat.txt",'w')
                if lista and awn['msg'] and awn['msg']!='\n':
                    # print("entrando com algo escrito")
                    arquivo.write(awn['msg']+"\n"+lista)
                elif awn['msg'] and awn['msg']!='\n':
                    # print("entrando com nada escrito")
                    arquivo.write(awn['msg'])
                else:
                    arquivo.write(lista)
                arquivo.close()
                dado=head("svr/chat/chat.txt",'204 No Content')
                conn.sendall(dado.encode())
               
 
                
        else:
            conn.sendall(b'HTTP/1.1 404 ERRO\n')
            conn.sendall(b'Connection: close\n')
            conn.sendall(b'Content-Type: text/html\n')
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
