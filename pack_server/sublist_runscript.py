from pack_server import sublist3r


def run(domain_name: str, rpt):
    s_domain = ''
    for sub in sublist3r.main(domain_name, 30, None, None, True, False, False, None):
        s_domain += sub + '\n'

    if s_domain:
        rpt.add_hn(2, 'Sub Domain List')
        rpt.add_cd(s_domain)
