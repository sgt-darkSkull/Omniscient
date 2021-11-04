def get_dorks(domain_name: str):
    from googlesearch import search
    
    info=list()
    dork = domain_name
    amount = 100
    interval = 2
    req = 0

    for i in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=int(interval)):
        info.append(i)
        req += 1
        if req >= int(amount):
            break
        
    return info


def run(domain_name: str):
    """returns list of the all the dorks"""
    return get_dorks(domain_name)
