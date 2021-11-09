from pack_server.dnsdmpstr import dnsdmpstr


def parse_hs(txt):

    rqry = txt.replace(',','\t:')
    return rqry


def get_info(target: str):
    dnsdump = dnsdmpstr()
    info = dict()
    info['rdns'] = parse_hs(dnsdump.hostsearch(target))+ parse_hs(dnsdump.reversedns(target))
    info['dnslookup'] = dnsdump.dnslookup(target)
    info['pagelinks'] = dnsdump.pagelinks(target)
    info['httpheaders'] = dnsdump.httpheaders(target)

    return info


def run(domain_name: str, rpt) :
    dnlkup = get_info(domain_name)
    if dnlkup:
        f_dnslookup = True
        rpt.add_hn(2, 'DNS Lookups')
        rpt.add_cd(dnlkup['dnslookup'])

        rpt.add_hn(2, 'Domain Resoultion')
        rpt.add_cd(dnlkup['rdns'])

        rpt.add_hn(2, 'HTTP Headers')
        rpt.add_cd(dnlkup['httpheaders'])

        rpt.add_hn(2, 'Links, You must look at')
        rpt.add_cd(dnlkup['pagelinks'])


