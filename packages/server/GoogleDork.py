try:
    from googlesearch import search
    from enum import Enum
except ImportError:
    print("Error importing search module...")


def get_dorks(domain_name: str):
    
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


if __name__ == "__main__":
    print(run('facebook.com'))
