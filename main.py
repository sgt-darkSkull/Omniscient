import colorama
from colorama import Fore, Back, Style
import argparse
import vuln_scanner
import p_person_ig
import p_server_ig


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=Fore.GREEN + "Omniscient Information Gatherer" + Fore.RESET)
    parser.add_argument("-A", "--active", help=Fore.BLUE + "For Active Scanning" + Fore.RESET, action="store_true")
    parser.add_argument("-P", "--passive", help=Fore.BLUE + "For Active Scanning" + Fore.RESET,
                        action="store_true")
    parser.add_argument("-H", "--host", type=str,
                        help=Fore.RED + "Hostname/Domain Name, incase of Server Scan" + Fore.RESET)
    parser.add_argument("-U", "--username", type=str,
                        help=Fore.RED + "Hostname/Domain Name, incase of Person Scan" + Fore.RESET)
    parser.add_argument("-o", "--output", type=str, help=Fore.GREEN + "Output File Name" + Fore.RESET)
    parser.add_argument("-T", "--type", type=str, help=Fore.GREEN + "Type of Scan [Server(S)/Person(P)]" + Fore.RESET)
    parser.add_argument("-k", "--shkey", type=str, help=Fore.GREEN + "" + Fore.RESET)
    arg = parser.parse_args()

    if not arg.active and not arg.passive:
        print(Fore.RED + "Specify Active (-A) or Passive Scanning (-P), At least one ARG should be passed\nCheck Help "
                         "menu, -h" + Fore.RESET)
        exit(-1)

    if arg.type not in ['s', 'p', 'S', 'P'] and arg.passive:
        print(Fore.RED + "The Scan Type must be in 'S' or 'P'\nCheck Help menu, -h" + Fore.RESET)
        exit(-1)

    if arg.type in ['p', 'P'] and not arg.username:
        print(Fore.RED + "Enter Username for Person, Scan\nCheck Help menu, -h" + Fore.RESET)
        exit(-1)

    if arg.active and arg.type in ['p', 'P']:
        print(Fore.RED + "Active Scanning is possible for Server only.\nNo need to specify" + Fore.RESET)
        exit(-1)

    if arg.active:
        vuln_scanner.run(arg.host)

    if arg.passive:

        if arg.type in ['s', 'S']:
            p_server_ig.run(arg.host, arg.shkey)
        if arg.type in ['p', 'P']:
            p_person_ig.run(arg.username, arg.output)

    # chain_run('Ishikawa-riva')
    #
    # # dao.insert('Users', {'Name': 'username'})
    # # user_id=int(dao.getuserid()[0][0])
    # # print(user_id)
    #
    # if not arg.linkedin and arg.type.lower() == "person":
    #     link_parser()
