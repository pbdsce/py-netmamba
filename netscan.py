#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import re

def banner():
    print(r"""     
                    dP                                  dP                
                    88                                  88                
88d888b. .d8888b. d8888P 88d8b.d8b. .d8888b. 88d8b.d8b. 88d888b. .d8888b. 
88'  `88 88ooood8   88   88'`88'`88 88'  `88 88'`88'`88 88'  `88 88'  `88 
88    88 88.  ...   88   88  88  88 88.  .88 88  88  88 88.  .88 88.  .88 
dP    dP `88888P'   dP   dP  dP  dP `88888P8 dP  dP  dP 88Y8888' `88888P8 """)
    print("\n********************************************************************")

def get_arguments():
    ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    ip_range = parser.parse_args()
    
    if not ip_range.target:
        parser.error("[-] Please specify a target IPv4 address/range, use --help for more info. (Example: --target 10.0.2.1/24 or --target 192.168.0.1/24)")
    if not ip_range_pattern.search(ip_range.target):
        parser.error("[-] Please enter a valid IPv4 address/range (Example: --target 10.0.2.1/24 or --target 192.168.0.1/24)")
    
    return ip_range

def scan_network(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_frame = broadcast/arp_packet # stacking of ARP packet and Ethernet frame
    response_list = scapy.srp(broadcast_frame, timeout=2, verbose=False)[0]
    clients_list = []
    for element in response_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


banner()
network_ip = get_arguments()
scan_result = scan_network(network_ip.target)
print_result(scan_result)