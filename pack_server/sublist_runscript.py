from pack_server import sublist3r


def run(domain_name: str, rpt):
    idx = 20
    s_domain = ''
    lst = sublist3r.main(domain_name, 30, None, None, True, False, False, None)
    for sub in lst:
        s_domain += sub + '\n'
        if not idx:
            break
        else:
            idx -= 1

    if s_domain:
        rpt.add_hn(2, 'Sub Domain List')
        rpt.add_cd(s_domain)
