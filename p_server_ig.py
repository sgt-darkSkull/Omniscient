import colorama
from pack_server import sublist_runscript as sl3r
from pack_server import shodan_lookup, netcraft_lookup, ddump, s_report


def run(target, sh_api):
    name = ''.join(target.split('.')[:-1])
    rpt = s_report.Report('Reports/', f'{name}.md', f"Omniscient Report for {target} \t\t\t[:SERVER:]")
    try:

        try:
            netcraft_lookup.run(target)
        except:
            pass
        try:
            ddump.run(target, rpt)
        except:
            pass
        try:
            sl3r.run(target, rpt)
        except:
            pass
        if sh_api is not None:
            try:
                shodan_lookup.run(target, sh_api, rpt)
            except:
                pass
        else:
            print("SHODAN Scan Require API KEY, Register at https://shodan.io to get Your API Key")
    except:
        print(colorama.Fore.RED + "Check Your Internet Connectivity" + colorama.Fore.RESET)
