from pack_server import sublist3r


def run(domain_name: str):
    return sublist3r.main(domain_name, 30, None, None, True, False, False, None)
