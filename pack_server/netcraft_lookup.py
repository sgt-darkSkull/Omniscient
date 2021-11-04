import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint


def get_info(domain_name: str) -> dict:
    """
        packet_structure
        {
            Background: {info}
            Network: {info} + ipdelegations
            HostingHistory= incomplete ( not able to target the table)

        }
        where each info is a dictionary


        domain_name with .com 

    """

    url = f"https://sitereport.netcraft.com/?url=http://www.{domain_name}"

    src = requests.get(url).content
    soup = BS(src, 'html.parser')

    info = dict()

    # background info
    section = soup.find_all('section', {"id": "background_table_section"})

    info['background'] = {}
    tables = section[0].findChildren('table', {"class": "table--list"})

    for table in tables:
        rows = table.findChildren('tr')
        for row in rows:
            title = row.findChildren('th')[0].text
            description = row.findChildren('td')[0].text
            info['background'][title] = description

    # network info

    section = soup.find_all('section', {"id": "network_table_section"})
    info['network'] = {}
    tables = section[0].findChildren('table', {"class": "table--list"})

    for table in tables:
        rows = table.findChildren('tr')
        for row in rows:
            title = row.findChildren('th')[0].text
            description = row.findChildren('td')[0].text
            info['network'][title] = description

    info['network']['ip_delegation'] = {}
    ips = section[0].findChildren('b')

    found_ips = []

    for ip in ips:
        if len(ip.text) > 1:
            info['network']['ip_delegation'][ip.text] = []
            found_ips.append(ip.text)

    tables = section[0].findChildren('table', {"class": "table-ipdel table--collapsible"})

    ip_counter = 0

    for table in tables:
        head = table.findChildren('thead')
        body = table.findChildren('tbody')
        body_rows = body[0].findChildren('tr')
        head_row = head[0].findChildren('th')

        ip = found_ips[ip_counter]
        ip_counter += 1

        for i in range(len(body_rows)):
            table_cells = body_rows[i].findChildren('td')
            info['network']['ip_delegation'][ip].append({})
            for j in range(len(head_row)):
                info['network']['ip_delegation'][ip][i][head_row[j].text] = table_cells[j].text

    return info


def run(domain_name: str) -> dict:
    return get_info(domain_name)


if __name__ == '__main__':
    pprint(run('facebook.com'))
    # print(run('facebook.com'))
