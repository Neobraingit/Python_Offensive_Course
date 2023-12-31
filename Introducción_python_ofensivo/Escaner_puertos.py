
#!/usr/bin/env python3

import socket
import argparse
import sys
import pdb
from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description = 'Fast TCP Port Scanner')
    parser.add_argument('-t', '--target', dest='target', help='Victim target to scan (Ex: -t 192.168.1.1)')
    parser.add_argument('-p', '--port', dest='port', help='Port range to scan (Ex: -p 1-100)')
    options = parser.parse_args()
    
    if not options.target:
        parser.print_help()
        sys.exit(1)
        
    return options.target

def create_socket():
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(1)
     return s
    

def port_scanner(port, host, s):
    try:
        s.connect((host, port))
        print (colored(f'\n[+] El puerto {port} está abierto¡', 'green'))
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
        
    
def main():
    target, port = get_arguments()
    if '-' in port:
        ports = port.split('-')
        pdb.set_trace()
    elif ',' in port:
        ports = port.split(',')
        
    for port in range(int(ports[0]), int(ports[1])):
        s = create_socket()
        port_scanner(port, target, s)
        
    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)
        
   
    
    
    
if __name__ == '__main__':
    main()
