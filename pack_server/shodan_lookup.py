import shodan
import socket


def get_info(domain_name: str, api_key: str) -> dict:
    ip = socket.gethostbyname(domain_name)
    api = shodan.Shodan(api_key)
    info = api.host(ip)
    return info


def run(domain_name: str, api_key: str) -> dict:
    return get_info(domain_name, api_key)
