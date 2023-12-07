
#!/usr/bin/env python3

import argparse
import subprocess
import sys


def get_arguments():
    parser = argparse.ArgumentParser(description='Herramienta para descubrir host activos en una red ICMP')
    parser.add_argument('-t', '--target', required=True, dest='target', help='Host o rango de IPS a escanear')
    
    args = parser.parse_args()
    return args.target

def parse_target(target_str):
    # 192.168.1.1-100
    target_str_splitted = target_str.split('.')
    first_three_octest = target_str_splitted[:3]
    
    if len(target_str_splitted) == 4:
        if '_' in target_str_splitted[:3]:
           start, end = target_str_splitted[3].split('_')
           return [f'{first_three_octest}.{i}' for i in range(int(start), int(end)+1)]
        else:
            return(target_str)
    else:
        print ('El rango de ip no es válido')
        
def host_discovery(targets):
    for target in targets:
        ping = subprocess.run(['ping', '-c', '1', target], timeout=1, stdout=subprocess.DEVNULL)
        
        if ping.returncode == 0:
            print (f'\t[i] La IP {target} está activa')
    

def main():
    target_str = get_arguments()
    targets = parse_target(target_str)
    
    print (f'\n[+] Host activos en la red:\n')
    host_discovery(targets)
    
    print (target_str)

if __name__ == '__main__':
    main ()