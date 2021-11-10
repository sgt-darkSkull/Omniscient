import shodan
import socket
from pack_server import s_report


def get_info(domain_name: str, api_key: str) -> dict:
    ip = socket.gethostbyname(domain_name)
    api = shodan.Shodan(api_key)
    info = api.host(ip)
    shodan_dct = dict()
    shodan_dct['region_code'] = info['region_code']
    shodan_dct['ip'] = info['ip']
    shodan_dct['postal_code'] = info['postal_code']
    shodan_dct['country_code'] = info['country_code']
    shodan_dct['city'] = info['city']
    shodan_dct['dma_code'] = info['dma_code']
    shodan_dct['last_update'] = info['last_update']
    shodan_dct['latitude'] = info['latitude']
    shodan_dct['tags'] = info['tags']
    shodan_dct['area_code'] = info['area_code']
    shodan_dct['country_name'] = info['country_name']
    shodan_dct['hostnames'] = info['hostnames']
    shodan_dct['org'] = info['org']
    shodan_dct['asn'] = info['asn']
    shodan_dct['isp'] = info['isp']
    shodan_dct['longitude'] = info['longitude']
    shodan_dct['country_code3'] = info['country_code3']
    shodan_dct['domains'] = info['domains']
    shodan_dct['ip_str'] = info['ip_str']
    shodan_dct['os'] = info['os']
    shodan_dct['ports'] = info['ports']
    return shodan_dct


def run(domain_name: str, api_key: str, rpt):

    shdn = get_info(domain_name, api_key)
    if shdn:
        rpt.add_hn(2, 'Shodan Scan Report (RAW)')
        rpt.add_cd(s_report.p_dict(shdn))


