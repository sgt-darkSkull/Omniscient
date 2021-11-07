import colorama

from pack_server import sublist_runscript as sl3r
from pack_server import shodan_lookup, netcraft_lookup, ddump, GoogleDork, s_report


def create_report(host, dnlkup, s_domain, dorks, shdn, ntcraft):
    name = ''.join(host.split('.')[:-1])
    rpt = s_report.Report('Reports/', f'{name}.md', f"Omniscient Report for {host} \t\t\t[:SERVER:]")

    f_dnslookup = False

    if dnlkup:
        f_dnslookup = True
        rpt.add_hn(2, 'DNS Lookups')
        rpt.add_cd(dnlkup['dnslookup'])

        rpt.add_hn(2, 'Domain Resoultion')
        rpt.add_cd(dnlkup['rdns'])

        rpt.add_hn(2, 'HTTP Headers')
        rpt.add_cd(dnlkup['httpheaders'])

    if s_domain:
        rpt.add_hn(2, 'Sub Domain List')
        rpt.add_cd(s_domain)

    if shdn:
        rpt.add_hn(2, 'Shodan Scan Report (RAW)')
        rpt.add_cd(s_report.p_dict(shdn))

    if dorks or f_dnslookup:
        rpt.add_hn(2, 'Links, You must look at')
        if f_dnslookup:
            rpt.add_cd(dnlkup['pagelinks'])
        elif f_dnslookup and dorks:
            rpt.add_cd(dorks + '\n' + dnlkup['pagelinks'])
        else:
            rpt.add_cd(dorks)


def run(target, sh_api):
    netcraft = dnsdump = dork = subdomains = shdn = None
    try:
        if sh_api is not None:
            shdn = shodan_lookup.run(target, sh_api)
        else:
            print("SHODAN Scan Require API KEY, Register at https://shodan.io to get Your API Key")

        # netcraft = netcraft_lookup.run(target)
        dnsdump = ddump.run(target)
        # dork = GoogleDork.run(target)
        subdomains = sl3r.run(target)
    except:
        print(colorama.Fore.RED + "Check Your Internet Connectivity" + colorama.Fore.RESET)
    create_report(target, dnsdump, subdomains, dork, shdn, netcraft)
    # create_report(target, shdn, '', 'dnsdump', 'dork', 'subdomains')


if __name__ == '__main__':
    print(sl3r.run('arowex.com'))
