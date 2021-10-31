#!/usr/bin/env python3

import sys
import json
import argparse
from dnsdmpstr import dnsdmpstr

parser = argparse.ArgumentParser()
parser.add_argument('-u', help="target domain")
parser.add_argument(
    '-a', help="host search (DNS A Record lookup)", action="store_true")
parser.add_argument(
    '-r', help="reverse dns lookup (accepts IP, IP range or domain name)", action="store_true")
parser.add_argument('-d', help="dns lookup", action="store_true")
parser.add_argument('-dd', help="classical dns dump format",
                    action="store_true")
parser.add_argument(
    '--links', help="grab page links from url", action="store_true")
parser.add_argument(
    '--headers', help="grab http headers from url", action="store_true")
parser.add_argument(
    '--all', help="grab all information available", action="store_true")
args = parser.parse_args()

dnsdump = dnsdmpstr()



def get_info(target: str):

	"""
	package structure:
	{
		hostsearch:
		reversedns:
		dnslookup:
		pagelinks:
		httpheaders:
	}
	"""





	info= dict()
	info['hostsearch']=dnsdump.hostsearch(target)
	info['reversedns']=dnsdump.reversedns(target)
	info['dnslookup']=dnsdump.dnslookup(target)
	info['pagelinks']=dnsdump.pagelinks(target)
	info['httpheaders']=dnsdump.httpheaders(target)

	return info





def run(domain_name:str)->dict:
		return get_info(domain_name)


if __name__=="__main__":
	 print(run('facebook.com'))