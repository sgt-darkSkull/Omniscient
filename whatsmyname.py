import json
import os
import WhatsMyName.check_online_presence as wmn_cop
import requests

if os.name == "posix":
    class Colors:
        YELLOW = "\033[93m"
        RED = "\033[91m"
        GREEN = "\033[92m"
        ENDC = "\033[0m"
else:
    class Colors:
        YELLOW = ""
        RED = ""
        GREEN = ""
        ENDC = ""


def warn(msg):
    print(Colors.YELLOW + msg + Colors.ENDC)


def error(msg):
    print(Colors.RED + msg + Colors.ENDC)


def positive(msg):
    print(Colors.GREEN + msg + Colors.ENDC)


def neutral(msg):
    print(msg)


def do_nothing(arg):
    pass


def check_username(user):
    # Suppress HTTPS warnings
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    # Online Websites Accounts
    web_file = 'WhatsMyName/web_accounts_list.json'
    with open(web_file) as data_file:
        data = json.load(data_file)

    sites_to_check = data['sites']

    try:
        for site in sites_to_check:
            if site['valid']:
                # INCOMPLETE
                wmn_cop.check_site(site, user,
                                   if_found=lambda url: positive("[+] User found at %s" % url),
                                   if_not_found=lambda url: do_nothing(url),
                                   if_neither=lambda url: error("[!] Error. The check implementation is broken "
                                                                "for %s" % url))
    except:
        pass


check_username('David')
