# #! /opt/Py3/bin/python
# import sys
# import argparse
# import subprocess
# import os
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from bs4 import BeautifulSoup as BS
#
# outstream = subprocess.DEVNULL
# errstream = subprocess.DEVNULL
#
# if arg.verbose:
#     outstream = None
#     errstream = None
#
# # Initiate
#
# if arg.ports == '-':
#     rcode = subprocess.call(f"nmap -p- -oX 'fullportscan.xml' -oN scanner.breifscan {arg.target} --min-rate=10000",
#                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
#     with open('fullportscan.xml', 'r') as fp:
#         data = fp.read()
#
#     xml = BS(data, 'xml')
#     ports = xml.findAll('port')
#
#     prts = ''
#     for port in ports:
#         prts += str(port['portid'])
#         prts += ','
#
#     prts = prts[:-1]
#     arg.ports = prts
#
#     os.remove('fullportscan.xml')
#
#     if (os.geteuid() == 0 or arg.force) and len(prts) > 0:
#         os.remove('scanner.breifscan')
#     else:
#         print("You are Adviced to run with sudo for detailed scan! ")
#         print("Breif Output is saved in scanner.breifscan")
#         exit()
#
# if arg.output == 'recon/ipscan':
#     if not os.path.isdir('recon'):
#         os.mkdir('recon')
#
# rcode = subprocess.call(
#     f"nmap -p{arg.ports} {arg.arguments} {arg.target} --min-rate={arg.rate} -o{arg.format} '{arg.output}'",
#     stdout=outstream, stderr=errstream, shell=True)


import subprocess, os
from bs4 import BeautifulSoup as BS
from colorama import Fore, Back, Style
import warnings


def get_open_ports_list(target):
    print(f"nmap -p- -oX '.temp.bin' {target} --min-rate=1000")
    rcode = subprocess.call(f"nmap -p- -oX '.temp.bin' {target} --min-rate=1000",
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    with open('.temp.bin', 'r') as fp:
        data = fp.read()

    xml = BS(data, 'xml')
    ports = xml.findAll('port')
    states = xml.findAll('state')
    prts = ''
    for i in range(len(ports)):
        if states[i]['state'] == 'open':
            prts += str(ports[i]['portid'])
            prts += ','

    prts = prts[:-1]
    ports = prts

    os.remove('.temp.bin')
    return ports


def web_service_scan(target, port):
    rcode = subprocess.call(f"nikto -host {target} -port {port}", shell=True)


def nmap_scan(target):
    # if os.geteuid() != 0:
    #     return None, None
    #
    open_ports = get_open_ports_list(target)
    print(open_ports)
    print(Fore.RED + "Nmap Scan Result .." + Style.RESET_ALL)
    print(
        f"sudo nmap -v -p{open_ports} -A -O -sV -sC --reason -T5 {target} --min-rate=100000 -oX .temp.bin --max-retries=1")
    prescan = subprocess.call(f"sudo nmap -v -p{open_ports} -A -O -sV -sC --reason -T5 {target} --min-rate"
                              f"=100000 -oX .temp.bin --max-retries=1", stdout=None, stderr=None, shell=True)

    # print(prescan.decode())
    print("\n\n")

    with open('.temp.bin', 'r') as fp:
        data = fp.read()

    xml = BS(data, 'xml')
    ports = xml.findAll('port')
    services = xml.findAll('service')
    os.remove('.temp.bin')

    return ports, services
    # scan = dict()
    # for i in range(len(ports)):
    #     print(ports[i]['portid'], services[i]['name'])


def run(target):
    ports, services = nmap_scan(target)
    if ports is not None:
        for i in range(len(services)):

            if 'http' in services[i]['name']:
                print(type(target), target, type(ports[i]['portid']), ports[i]['portid'])
                web_service_scan(target, ports[i]['portid'])
    else:
        raise Exception("Require root Permissions")


if __name__ == '__main__':
    # print(type(get_open_ports_list('127.0.0.1')))
    run('10.0.2.14')
    # run('127.0.0.1')
    # run('facebook.com')
