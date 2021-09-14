import json

import WhatsMyName.check_online_presence as wmn_cop
import requests

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
            pass
    except:
        pass