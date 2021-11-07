from pack_server import sublist3r


def run(domain_name: str):
    s_lst = ''
    for sub in sublist3r.main(domain_name, 30, None, None, True, False, False, None):
        s_lst += sub + '\n'

    return s_lst
