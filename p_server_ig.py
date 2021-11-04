from pack_server import sublist_runscript as sl3r
from pack_server import shodan_lookup, netcraft_lookup, ddump, GoogleDork, s_report


def create_report(host, shdn, ntcraft, dns, dorks, s_domain):
    rpt = s_report.Report('Reports', f'{host}.md', f"Omniscient Report for {host}\t\t[:SERVER:]")


def run(target, sh_api):
    shdn = None
    if sh_api is not None:
        shdn = shodan_lookup.run(target, sh_api)
    else:
        print("SHODAN Scan Require API KEY, Register at https://shodan.io to get Your API Key")

    netcraft = netcraft_lookup.run(target)
    dnsdump = ddump.run(target)
    dork = GoogleDork.run(target)
    subdomains = sl3r.run(target)
    create_report(target, shdn, netcraft, dnsdump, dork, subdomains)
    # print(target, shdn, netcraft, dnsdump, dork, subdomains)


# if __name__ == '__main__':
    # run('google.com', '0AN48qkw7sEMiY38K9lFut8BweZU8IBi')
