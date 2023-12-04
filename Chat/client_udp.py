
#!/usr/bin/env python3
import socket

def client_udp():
    host = 'localhost'
    port = 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = 'Hola se está tensado muchísimo'.encode('utf-8')
        s.sendto(message,(host, port))
    
    
client_udp()