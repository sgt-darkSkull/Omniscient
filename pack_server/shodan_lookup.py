import shodan
import socket
from pack_server import s_report


def get_info(domain_name: str, api_key: str) -> dict:
    ip = socket.gethostbyname(domain_name)
    api = shodan.Shodan(api_key)
    info = api.host(ip)
    return info


def run(domain_name: str, api_key: str, rpt):

    shdn = get_info(domain_name, api_key)
    if shdn:
        rpt.add_hn(2, 'Shodan Scan Report (RAW)')
        rpt.add_cd(s_report.p_dict(shdn))


