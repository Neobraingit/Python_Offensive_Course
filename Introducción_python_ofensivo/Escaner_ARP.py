
#!/usr/bin/env python3

import scapy.all as scapy

import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='ARP Scanner')
    parser.add_argument('-t', '--target', required=True, dest='target', help='Hostm/ IP Range To Scan')
    
    args = parser.parse_args()
    return args.target()

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    
    arp_packet = broadcast_packet/arp_packet
    
    answered, unsanswered =scapy.srp(arp_packet)
    
    response = answered.summary()
    if response:
        print (response)
    
    print (answered)
    print (unsanswered)
 

def main():
    target = get_arguments()
    
    
if __name__ == '__main__':
    main()
