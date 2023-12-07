
#!/usr/bin/env python3

import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Herramienta para descubrir host activos en una red ICMP')
    parser.add_argument('-t', '--target', required=True, dest='target', help='Host o rango de IPS a escanear')
    
    args = parser.parse_args()
    return args.target

def parse_target(target_str):
    # 192.168.1.1-100
    target_str_splitted = target_str.split('.')
    first_three_octest = target_str_splitted[:3]

def main():
    target_str = get_arguments()
    targets = parse_target(target_str)
    
    print (target_str)

if __name__ == '__main__':
    main ()