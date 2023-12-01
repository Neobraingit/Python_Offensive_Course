
#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # aceptamos conexiones entrantes 
server_addres= ('localhost', 1234) # definimos la direccion y el puerto de escucha
server_socket.bind(server_addres) 

# Límite de conexiones
server_socket.listen(1)
while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)
    
    print (f'\n[+] Mensaje recibido del cliente: {data.decode()}')
    print (f'\n[+] Información del cliente que se ha conectado: {client_address}')
    
    client_socket.sendall(f'Un saludo crack\n'.encode())
    client_socket.close()