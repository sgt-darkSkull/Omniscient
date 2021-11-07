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


def run(domain_name: str) -> dict:
    return get_info(domain_name)

