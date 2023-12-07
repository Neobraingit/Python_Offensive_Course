
#!/usr/bin/env python3

print ('---------- Macchanger ---------------')

import argparse
import re
import subprocess
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description='Herramienta para cambiar la mac de una interfaz de red')
    parser.add_argument('-i', '--interface', required = True, dest=' Interface', help = 'Nombre de la interfaz de red')
    parser.add_argument('-m', '--mac', required=True, dest='mac_address', help='Nueva dirección MAC para la interface de red')

    return parser.parse_args()

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^[e][n]\d{0}', interface)
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]{5})[A-Fa-f0-9]$', mac_address)
    print (colored(f'\n[+] La mac ha sido cambiada exitoramente', 'red'))
    

def change_mac_address(interface, mac_adrdress):
    if is_valid_input(interface, mac_adrdress):
        subprocess.run(['ifconfig', interface, 'down'])
        subprocess.run(['ifconfig', interface, 'hw', 'ether', mac_adrdress])
        subprocess.run (['ifconfig', interface, 'up'])
        print ('Se tensa')
        
        
    

def main():
    args = get_arguments()
    
    change_mac_address(args.interface, args.mac_address)

if __name__ == '__main__':
    main()