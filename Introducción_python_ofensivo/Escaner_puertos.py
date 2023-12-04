
#!/usr/bin/env python3

import socket

host = '192.168.1.1'
port = 80


def port_scanner():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((host, port)):
        print (f'\n[+] El puerto {port} está abierto.')
    else:
        print (f'\n[!] El puerto {port} está cerrado.')
    

def main():
    port_scanner(port)
    
if __name__ == '__main__':
    main()