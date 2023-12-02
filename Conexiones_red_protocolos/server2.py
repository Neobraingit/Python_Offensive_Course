from collections.abc import Callable, Iterable, Mapping
import socket
import threading
from typing import Any

class ClientThread(threading.Thread):
    def __init__(self, client_sock, client_sddr):
        super().__init__()
        self.client_sock = client_sock
        self.client_sddr =client_sddr
        
        print (f'\n[+] Nuevo cliente conectado: {client_sddr}')
        
    def run(self):
        message = ''
        
        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()
            
            if message.strip() == 'bye':
                break
            
            print (f'\n[+] Mensaje enviado por el cliente: {message} ')
            self.client_sock.send(data)
            
        print (f'\n[!] Cliente {self.client_sddr} desconectado...')
        self.client_sock.close()
        
HOST = 'localhost'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
    server_socket.bind((HOST, PORT))
    print (f'\n[+] En espera de conexiones entrantes...')
    
    while True:
        server_socket.listen()
        client_sock, client_sddr = server_socket.accept()
        new_thread = ClientThread(client_sock, client_sddr)
        new_thread.start()