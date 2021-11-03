import requests
from bs4 import BeautifulSoup as BS
import pprint


def get_info(domain_name: str) -> dict:
    """
        packet_structure
        {
            domain_information: info
            Registrant Contact: info
            Administrative_Contact: info
            Technical Contact: info
            RawWhoisData: info

        }
        where each info is a dictionary


        domain_name with .com 

    """

    url = f"https://www.whois.com/whois/{domain_name}"

    src = requests.get(url).content
    soup = BS(src, 'html.parser')

    info = dict()

    info_blocks = soup.find_all('div', {"class": "df-block"})

    for block in info_blocks:
        heading = block.findChildren('div', {"class": "df-heading"})[0].text
        info[heading] = {}

        rows = block.findChildren('div', {"class": "df-row"})

        for inside_info in rows:
            label = inside_info.findChildren('div', {"class": "df-label"})[0].text
            value = inside_info.findChildren('div', {"class": "df-value"})[0].text
            info[heading][label] = value

    raw_whoisdata = soup.find_all('div', {"class": "df-block-raw"})
    raw_heading = raw_whoisdata[0].findChildren('div', {"class": "df-heading"})[0].text
    raw_content = raw_whoisdata[0].findChildren('pre', {"id": "registrarData"})[0].text

    info[raw_heading] = raw_content

    return info


def run(domain_name: str) -> dict:
    return get_info(domain_name)


if __name__ == '__main__':
    print(run('facebook.com'))
