from pack_server import sublist_runscript as sl3r
from pack_server import shodan_lookup, netcraft_lookup, ddump, GoogleDork


def report():
    pass


def run(target, sh_api):
    shdn = None
    if sh_api is not None:
        shdn = shodan_lookup.run(target, sh_api)
    else:
        print("SHODAN Scan Require API, KEY, Register and get FREE api on shodan.com")

    netcraft = netcraft_lookup.run(target)
    dnsdump = ddump.run(target)
    dork = GoogleDork.run(target)
    subdomains = sl3r.run(target)


if __name__ == '__main__':
    print(run('google.com', '0AN48qkw7sEMiY38K9lFut8BweZU8IBi'))
