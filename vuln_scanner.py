#! /opt/Py3/bin/python
import sys
import argparse
import subprocess
import os
import nmap
from bs4 import BeautifulSoup as BS

parser = argparse.ArgumentParser(description='Automated Nmap Scanner (Active Information Gathering)')
parser.add_argument("-t", "--target", type=str, help="targeted IP address", required=True)
parser.add_argument("-p", "--ports", type=str, help="ports to scan (Default range = 0-65535)", default='-')
parser.add_argument("-a", "--arguments", type=str, help="nmap scan arguments (Default -sC -sV -O -A )",
                    default='sC -sV -O -A')
parser.add_argument("-r", "--rate", type=str, help="min Rate (Default 10000)", default='10000')
parser.add_argument("-o", "--output", type=str, help="output file(Default recon/ipscan)", default='recon/ipscan')
parser.add_argument("-f", "--format", type=str,
                    help="output Format[A,N,G,X] (Default 'A', All Format {standard, Grepable, xml})", default='A')
parser.add_argument("-v", "--verbose", help="print scan output on screen", action="store_true")
parser.add_argument("--force", help="ignore warnings", action="store_true")

arg = parser.parse_args()

if (len(arg.arguments)):
    arg.arguments = '-' + arg.arguments

outstream = subprocess.DEVNULL
errstream = subprocess.DEVNULL

if arg.verbose:
    outstream = None
    errstream = None

# Initiate

if arg.ports == '-':

    ps = nmap.PortScanner()
    rcode = subprocess.call(f"nmap -p- -oX 'fullportscan.xml' -oN scanner.breifscan {arg.target} --min-rate=10000",
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    with open('fullportscan.xml', 'r') as fp:
        data = fp.read()

    xml = BS(data, 'xml')
    ports = xml.findAll('port')

    prts = ''
    for port in ports:
        prts += str(port['portid'])
        prts += ','

    prts = prts[:-1]
    arg.ports = prts

    os.remove('fullportscan.xml')

    if (os.geteuid() == 0 or arg.force) and len(prts) > 0:
        os.remove('scanner.breifscan')
    else:
        print("You are Adviced to run with sudo for detailed scan! ")
        print("Breif Output is saved in scanner.breifscan")
        exit()

if arg.output == 'recon/ipscan':
    if not os.path.isdir('recon'):
        os.mkdir('recon')

rcode = subprocess.call(
    f"nmap -p{arg.ports} {arg.arguments} {arg.target} --min-rate={arg.rate} -o{arg.format} '{arg.output}'",
    stdout=outstream, stderr=errstream, shell=True)
