import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 10239
name = input("昵称: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def ServerThread():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')  
            if msg == '昵称：':                           
                client.send(name.encode('utf-8'))    
            else:
                print(msg)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:  
        msg = '{}: {}'.format(name, input(''))
        client.send(msg.encode('utf-8'))

server_thread = threading.Thread(target=ServerThread)
server_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start() 