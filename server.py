import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 10239

clients = [] 
names = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
server.bind((HOST, PORT))                                          
server.listen()

def PublishMsg(msg):
    for c in clients:
        c.send(msg)

def ClientThread(client):
    while True:
        try:
            msg = client.recv(1024)                      
            PublishMsg(msg)          
        except:
            index = clients.index(client)        
            clients.remove(client)       
            client.close()
            name = names[index]
            PublishMsg('{} left!'.format(name).encode('utf-8'))  
            names.remove(name)
            break

def LoopListenAccept():
    while True:
        client, address = server.accept()                        
        print("Connected with {}".format(str(address)))           

        client.send('昵称：'.encode('utf-8'))                       
        name = client.recv(1024).decode('utf-8')                
        names.append(name)
        clients.append(client)

        print("Name is {}".format(name))

        PublishMsg("{} 加入了!".format(name).encode('utf-8'))  
        client.send('Connected to server!'.encode('utf-8'))        

        thread = threading.Thread(target=ClientThread, args=(client,))   
        thread.start()

print("Server start")
LoopListenAccept()