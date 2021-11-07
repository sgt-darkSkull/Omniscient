from colorama import Fore, Back, Style
import argparse


def main():
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
    parser.add_argument("-k", "--shkey", type=str, help=Fore.GREEN + "Enter SHODAN API Personal key" + Fore.RESET)
    parser.add_argument("--no-linkedin", help=Fore.GREEN + "Passive Person Scan, No linkedin data" + Fore.RESET,
                        action="store_true")
    arg = parser.parse_args()

    if not arg.active and not arg.passive:
        print(Fore.RED + "Specify Active (-A) or Passive Scanning (-P), At least one ARG should be passed\nCheck Help "
                         "menu, -h" + Fore.RESET)
        exit(-1)

    if arg.type not in ['s', 'p', 'S', 'P'] and arg.passive:
        print(Fore.RED + "The Scan Type must be in 'S' or 'P'\nCheck Help menu, -h" + Fore.RESET)
        exit(-1)

    if arg.type in ['p', 'P'] and not arg.username:
        arg.username = input("Username not Provided,\nEnter Username >>> " + Fore.RESET)

    if arg.type in ['s', 'S'] and not arg.host:
        arg.host = input("Host not Provided,\nEnter Host >>> " + Fore.RESET)

    if arg.active and arg.type in ['p', 'P']:
        print(Fore.RED + "Active Scanning is possible for Server only.\nNo need to specify" + Fore.RESET)
        exit(-1)

    if arg.active:
        import vuln_scanner

        if arg.host is None:
            arg.host = input("Host Not Provided, \nEnter Remote Host Address to scan >>> ")
        vuln_scanner.run(arg.host)

    if arg.passive:
        if arg.type in ['s', 'S']:
            import p_server_ig

            p_server_ig.run(arg.host, arg.shkey)
        elif arg.type in ['p', 'P']:
            import p_person_ig

            p_person_ig.run(arg.username, arg.output, arg.no_linkedin)


if __name__ == '__main__':
    # main()
    try:
        main()
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + Back.LIGHTWHITE_EX + "\t  Exception Caught!  \t" + Style.RESET_ALL)
