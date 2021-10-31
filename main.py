# Modules:
#
#     Codechef
#         name
#         id
#         location
#         bio
#         LinkIN ID
#     Github
#             Login Name : login
#         2.  User Github ID: id
#         3.  Avatar : avatar_url
#         4.  Following : following_url
#         5.  Name: name
#         6.  Company: company
#         7.  Blog:   blog
#         8.  Location: location
#         9.  Email: email
#         10. Job Req: hireable
#         11. Bio: bio
#         12. Twitter: twitter_username
#     Hacker Rank
#         1.  Login Name : userid
#         2.  Name: name
#         3.  Location: location
#         4.  Bio: bio
#         5.  LinkedIN ID: lnkid
#     Instagram
#         1.  Login Name : userid
#         2.  Name: name
#         3. Bio: bio
#     Twitter
#         1.  Login Name : userid
#         2.  Name: name
#         3.  Location: location
#         4.  Bio: bio


'''

1. Website
2. Target User
3. Choice
4.

'''

from colorama import Fore, Back, Style
import argparse
from packages import dao

from packages import github, codechef, coroflot, dev_community, ello, \
    face, flickr, freelancer, gravatar, hackaday, hackerrank, instagram, mal, \
    newgrounds, pinkbike, reddit, soundcloud, twitter, typeracer, ultimate_guitar, vimeo


def chain_run(username):
    dao.insert('Users', {'Name': 'username'})
    user_id=int(dao.getuserid()[0][0])
    # print(user_id)
    github.run(username, user_id)
    codechef.run(username, user_id)
    coroflot.run(username, user_id)
    dev_community.run(username, user_id)
    ello.run(username, user_id)
    face.run(username, user_id)
    freelancer.run(username, user_id)
    gravatar.run(username, user_id)
    hackaday.run(username, user_id)
    hackerrank.run(username, user_id)
    instagram.run(username, user_id)
    mal.run(username, user_id)
    pinkbike.run(username, user_id)
    reddit.run(username, user_id)
    soundcloud.run(username, user_id)
    twitter.run(username, user_id)
    typeracer.run(username, user_id)
    ultimate_guitar.run(username, user_id)
    vimeo.run(username, user_id)


# LinkedIn Input Information Parser
def link_parser():
    print(
        Fore.RED + "For better results Follow The Target User on Linked in and save their profile info - " + Style.RESET_ALL)
    print(Fore.RED + "Give NA as input if Answer is not known.." + Style.RESET_ALL)
    print('')
    if input("Want to Input LinkedIN Information : ").lower() == ("y" or "yes"):
        lname = input("Enter Target's Name, Full Name : ")
        lclg = input("Enter Target's College Name : ")
        email = input("Enter Target's Email : ")
        phno = input("Enter Target's PHNO : ")
        bday = input("Enter Target's Date of Birth : ")
        adrs = input("Enter Target Address : ")
        lnk_adr = input("Enter Target's LinkedIn Profile URL : ")


def run():
    pass


if __name__ == '__main__':
    chain_run('Ishikawa-riva')
    parser = argparse.ArgumentParser(
        description=Fore.GREEN + "Omniscient Passive Information Gatherer" + Style.RESET_ALL)
    parser.add_argument("-t", "--type", type=str,
                        help=Fore.RED + "Type of Information Scan [Person/Server]" + Style.RESET_ALL, required=True)
    parser.add_argument("-L", "--linkedin", type=str,
                        help=Fore.CYAN + "Linkedin Information JSON File" + Style.RESET_ALL)
    parser.add_argument("-f", "--format", help=Fore.BLUE + "Select Output File Format (PDF/JSON/TXT)" + Style.RESET_ALL,
                        default="PDF")
    parser.add_argument("-out", type=str, help=Fore.RED + "Output File Name" + Style.RESET_ALL, required=True)
    parser.add_argument("-u", "--username", type=str, help=Fore.GREEN + "Target Username" + Style.RESET_ALL)
    parser.add_argument("-d", "--domain", type=str, help=Fore.GREEN + "Target Domain Name" + Style.RESET_ALL)

    arg = parser.parse_args()

    # dao.insert('Users', {'Name': 'username'})
    # user_id=int(dao.getuserid()[0][0])
    # print(user_id)

    if not arg.linkedin and arg.type.lower() == "person":
        link_parser()
