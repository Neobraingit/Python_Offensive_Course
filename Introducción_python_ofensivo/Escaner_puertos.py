
#!/usr/bin/env python3

import socket
import argparse
import sys
from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description = 'Fast TCP Port Scanner')
    parser.add_argument('-t', '--target', dest='target', help='Victim target to scan (Ex: -t 192.168.1.1)')
    options = parser.parse_args()
    
    if not options.target:
        print (colored(f'\n[!] No se ha proporcionado el target', 'red'))
        sys.exit(1)
        
    return options.target

def create_socket():
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(1)
     return s
    

def port_scanner(port, host, s):
    try:
        s.connect((host, port))
        print (colored(f'\n[+] El puerto {port} está abierto¡', 'red'))
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
        
    
def main():
    target = get_arguments()
    for port in range(1, 1000):
        s = create_socket()
        port_scanner(port, target, s)
    
    
if __name__ == '__main__':
    main()