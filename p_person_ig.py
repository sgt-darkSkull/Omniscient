from colorama import Fore, Back, Style
from pack_person import p_report
from pack_person import github, codechef, coroflot, dev_community, ello, face, freelancer, gravatar, hackaday, \
    hackerrank, instagram, mal, pinkbike, reddit, soundcloud, twitter, typeracer, ultimate_guitar, vimeo, data_access_object


def chain_run(username):
    dao = data_access_object.DAO()
    dao.main()
    rpt = p_report.Report("Reports/", f'{username}.md', f"Omniscient Report for {username} \t\t\t")
    dao.insertU('Users', {'Name': 'username'}, )
    user_id = int(dao.getuserid()[0][0])
    try:
        github.run(username, user_id, rpt, dao)
    except:
        pass
    try:
        codechef.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        coroflot.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        dev_community.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        ello.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        face.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        freelancer.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        gravatar.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        hackaday.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        hackerrank.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        instagram.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        mal.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        pinkbike.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        reddit.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        soundcloud.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        typeracer.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        ultimate_guitar.run(username, user_id, rpt, False, dao)
    except:
        pass
    try:
        vimeo.run(username, user_id, rpt, False, dao)
    except:
        pass
    dao.conn.close()


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


def run(target, output= None, lreq=False):
    if not lreq:
        link_parser()
    chain_run(target)

