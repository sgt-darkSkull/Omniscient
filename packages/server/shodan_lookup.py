import shodan
import socket
from pprint import pprint
import json


def get_info(domain_name: str , api_key : str) -> dict:
    ip = socket.gethostbyname(domain_name)
    api = shodan.Shodan(api_key)

    info = api.host(ip)

    return info


def run(domain_name: str,api_key: str) -> dict:
    return get_info(domain_name,api_key)


if __name__ == '__main__':
    pprint(run('facebook.com','0AN48qkw7sEMiY38K9lFut8BweZU8IBi'))
    # print(run('facebook.com'))
