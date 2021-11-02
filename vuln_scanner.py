import subprocess, os
from bs4 import BeautifulSoup as BS
from colorama import Fore, Back, Style


def get_open_ports_list(target):
    print(Fore.BLUE + f"[*] Getting Open Ports for the Address : {target}" + Style.RESET_ALL)
    rcode = subprocess.call(f"nmap -p- -oX '.temp.bin' {target} --min-rate=1000000",
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    with open('.temp.bin', 'r') as fp:
        data = fp.read()

    xml = BS(data, 'xml')
    ports = xml.findAll('port')
    states = xml.findAll('state')

    if len(ports) > 40:
        print(Fore.RED + f"[-] Can not perform Network Scan on {target}\n" + Style.RESET_ALL)
        return None

    prts = ''
    for i in range(len(ports)):
        if states[i]['state'] == 'open' :
            prts += str(ports[i]['portid'])
            prts += ','

    prts = prts[:-1]
    ports = prts

    print(Fore.GREEN + f"[+] Open Ports ({target}) : {ports}\n\n" + Style.RESET_ALL)

    os.remove('.temp.bin')
    return ports


def web_service_scan(target, port, ssl=False):

    if ssl:
        ssl = 'https'
        print(Fore.RED + "[.] HTTPS Service Found" + Style.RESET_ALL)
    else:
        ssl = 'http'

    print(Fore.BLUE + "[*] Getting Server Configurations.. RUNNING Wappalyzer" + Style.RESET_ALL)
    wappalyzer = subprocess.check_output(f'wappalyzer {ssl}://{target}:{port}/ --pretty', shell=True).decode()

    print(wappalyzer)

    print(Fore.GREEN + "[+] Wappalyzer Scan Completed\n" + Style.RESET_ALL)

    if 'wordpress' in wappalyzer:
        print(Fore.GREEN + "[+] Wordpress CMS Detected.., " + Style.RESET_ALL)
        print(Fore.BLUE + "[*] Starting wpscan\n" + Style.RESET_ALL)

        rcode = subprocess.call(f'wpscan --url {ssl}://{target}:{port}', shell=True)

        print(Fore.GREEN + "[+] Wordpress scan Completed\n" + Style.RESET_ALL)

    print(Fore.BLUE + "[*] Running Final Web Vulnerability Scanner" + Style.RESET_ALL)
    print(Fore.MAGENTA + "[!] This Scan may Take Time, depending on your system config and Link Speed.." + Style.RESET_ALL)
    rcode = subprocess.call(f"nikto -host {target} -port {port} -timeout 2", shell=True)

    if '"status": 30' in wappalyzer:
        return False
    else:
        return True


def nmap_scan(target):
    # if os.geteuid() != 0:
    #     return None, None

    open_ports = get_open_ports_list(target)

    if open_ports is None or len(open_ports) < 1:
        return 'NWSCANERR', 'NWSCANERR'
    print(Fore.BLUE + "[*] Starting Network Scanner (NMAP).." + Style.RESET_ALL)
    prescan = subprocess.call(f"sudo nmap -p{open_ports} -A -O -sV -sC --reason -T5 --min-rate=100000 "
                              f"-oX .temp.bin --max-retries=1 {target}", stdout=None, stderr=None, shell=True)

    print(Fore.BLUE + "[+] Network Scanning Completed \n" + Style.RESET_ALL)

    with open('.temp.bin' , 'r') as fp:
        data = fp.read()

    xml = BS(data, 'xml')
    ports = xml.findAll('port')
    services = xml.findAll('service')
    os.remove('.temp.bin')

    return ports, services


def run(target):
    ports, services = nmap_scan(target)
    if ports == 'NWSCANERR':
        print(Fore.RED + f"[-] Using Brute Scanner for Web Services" + Style.RESET_ALL)
        print(Fore.RED + f"[*] Initiating Blind HTTP Web Scan On {target} .... [CONFIG : DEFAULT]" + Style.RESET_ALL)
        if web_service_scan(target,80):
            print('')
            print(Fore.RED + f"[*] Initiating Blind HTTPS Web Scan On {target} .... [CONFIG : DEFAULT]" + Style.RESET_ALL)
            web_service_scan(target,443, True)
        else:
            print('')
            print(Fore.RED + f"[+] SSL Redirection is SET to TRUE, Skipping.. HTTPS Scan" + Style.RESET_ALL)
        print('')
    elif ports is not None:
        for i in range(len(services)):

            if 'http' in services[i]['name']:
                flag = False
                if 'https' in services[i]['name']:
                    flag = True
                print(Fore.BLUE + f"[*] Starting Scan for Web Vulnerabilities for PORT : {ports[i]['portid']}" + Style.RESET_ALL)
                web_service_scan(target, ports[i]['portid'], flag)
                print(Fore.GREEN + f"[+] Vulnerabilities Scan Completed for PORT : {ports[i]['portid']}\n" + Style.RESET_ALL)
    else:
        raise Exception("Require root Permissions")


if __name__ == '__main__':
    # print(type(get_open_ports_list('127.0.0.1')))
    run('10.0.2.14')
    # run('techcrunch.com')
    # run('127.0.0.1')
    # run('facebook.com')
    # web_service_scan('10.0.2.14', '80')
    # web_service_scan('techcrunch.com', '443', True)
