from colorama import Fore, Back, Style
from pack_person import p_report
from pack_person import github, codechef, coroflot, dev_community, ello, face, freelancer, gravatar, hackaday, \
    hackerrank, instagram, mal, pinkbike, reddit, soundcloud, twitter, typeracer, ultimate_guitar, vimeo, dao


def chain_run(username):
    rpt = p_report.Report("Reports/", f'{username}.md', f"Omniscient Report for {username} \t\t\t")
    dao.insertU('Users', {'Name': 'username'}, )
    user_id = int(dao.getuserid()[0][0])
    github.run(username, user_id, rpt)
    codechef.run(username, user_id, rpt)
    coroflot.run(username, user_id, rpt)
    dev_community.run(username, user_id, rpt)
    ello.run(username, user_id, rpt)
    face.run(username, user_id, rpt)
    freelancer.run(username, user_id, rpt)
    gravatar.run(username, user_id, rpt)
    hackaday.run(username, user_id, rpt)
    hackerrank.run(username, user_id, rpt)
    instagram.run(username, user_id, rpt)
    mal.run(username, user_id, rpt)
    pinkbike.run(username, user_id, rpt)
    reddit.run(username, user_id, rpt)
    soundcloud.run(username, user_id, rpt)
    typeracer.run(username, user_id, rpt)
    ultimate_guitar.run(username, user_id, rpt)
    vimeo.run(username, user_id, rpt)


# LinkedIn Input Information Parser
def link_parser():
    print(
        Fore.RED + "For better results Make connection with Target User on Linkedin and save their profile info - " + Fore.RESET)
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


def run(target, output, lreq=False):
    if not lreq:
        link_parser()
    chain_run(target)
