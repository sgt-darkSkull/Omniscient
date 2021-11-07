def get_dorks(domain_name: str):
    from googlesearch import search

    dorks = ''
    tld = domain_name.split('.')[-1]
    amount = 30
    interval = 2
    req = 0

    for i in search(domain_name, tld=tld, lang="en", num=int(amount), start=0, stop=30, pause=int(interval)):
        dorks += dorks + i + '\n'
        req += 1
        if req >= int(amount):
            break
    return dorks


def run(domain_name: str):
    """returns list of the all the dorks"""
    return get_dorks(domain_name)

