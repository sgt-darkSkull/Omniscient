from pack_server.dnsdmpstr import dnsdmpstr


def parse_hs(txt):

    lst = txt.split('\n')[:15]
    txt = '\n'.join(['', *lst, ''])

    rqry = txt.replace(',','\t:').replace('\\n\\n','\\n')
    return rqry


def get_info(target: str):
    dnsdump = dnsdmpstr()
    info = dict()
    info['rdns'] = (parse_hs(dnsdump.reversedns(target)) + parse_hs(dnsdump.hostsearch(target))).strip()
    info['dnslookup'] = dnsdump.dnslookup(target)
    info['pagelinks'] = dnsdump.pagelinks(target)
    info['httpheaders'] = dnsdump.httpheaders(target)

    return info


def run(domain_name: str, rpt) :
    dnlkup = get_info(domain_name)
    if dnlkup:
        rpt.add_hn(2, 'DNS Lookups')
        rpt.add_cd(dnlkup['dnslookup'])

        rpt.add_hn(2, 'Domain Resoultion')
        rpt.add_cd(dnlkup['rdns'])

        rpt.add_hn(2, 'HTTP Headers')
        rpt.add_cd(dnlkup['httpheaders'])

        rpt.add_hn(2, 'Links, You must look at')
        rpt.add_cd(dnlkup['pagelinks'])


