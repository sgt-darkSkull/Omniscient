from pack_server.dnsdmpstr import dnsdmpstr


def get_info(target: str):
    dnsdump = dnsdmpstr()
    info = dict()
    info['hostsearch'] = dnsdump.hostsearch(target)
    info['reversedns'] = dnsdump.reversedns(target)
    info['dnslookup'] = dnsdump.dnslookup(target)
    info['pagelinks'] = dnsdump.pagelinks(target)
    info['httpheaders'] = dnsdump.httpheaders(target)

    return info


def run(domain_name: str) -> dict:
    return get_info(domain_name)


if __name__ == "__main__":
    print(run('facebook.com'))
