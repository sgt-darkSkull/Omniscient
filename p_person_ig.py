from colorama import Fore, Back, Style
from pack_person import github, codechef, coroflot, dev_community, ello, face, freelancer, gravatar, hackaday, \
    hackerrank, instagram, mal, pinkbike, reddit, soundcloud, twitter, typeracer, ultimate_guitar, vimeo, dao


def chain_run(username):
    dao.insert('Users', {'Name': 'username'})
    user_id = int(dao.getuserid()[0][0])
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
    # twitter.run(username, user_id)
    typeracer.run(username, user_id)
    ultimate_guitar.run(username, user_id)
    vimeo.run(username, user_id)


# LinkedIn Input Information Parser
def link_parser():
    print(Fore.RED + "For better results Make connection with Target User on Linkedin and save their profile info - " + Fore.RESET)
    print(Fore.RED + "Give NA as input if Answer is not known.." + Fore.RESET)
    print('')
    if input("Want to Input Linkedin Information : ").lower() == ("y" or "yes"):
        lname = input("Enter Target's Name, Full Name : ")
        lclg = input("Enter Target's College Name : ")
        email = input("Enter Target's Email : ")
        phno = input("Enter Target's PHNO : ")
        bday = input("Enter Target's Date of Birth : ")
        adrs = input("Enter Target Address : ")
        lnk_adr = input("Enter Target's LinkedIn Profile URL : ")


def run(target, output, lreq = False):
    if not lreq:
        link_parser()
    chain_run(target)
