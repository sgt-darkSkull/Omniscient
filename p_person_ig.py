from colorama import Fore, Back, Style
from pack_person import p_report
from pack_person import github, codechef, coroflot, dev_community, ello, face, freelancer, gravatar, hackaday, \
    hackerrank, instagram, mal, pinkbike, reddit, soundcloud, twitter, typeracer, ultimate_guitar, vimeo, data_access_object


def chain_run(username, rpt, dao):

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
    info = dict()
    if input("Want to Input Linkedin Information : ").lower() == ("y" or "yes"):
        info['Link_name'] = input("Enter Target's Name, Full Name : ")
        info['Link_clg'] = input("Enter Target's College Name : ")
        info['Link_email'] = input("Enter Target's Email : ")
        info['Link_phno'] = input("Enter Target's PHNO : ")
        info['Link_DOB'] = input("Enter Target's Date of Birth : ")
        info['Link_adrs'] = input("Enter Target Address : ")
        info['Link_link'] = input("Enter Target's LinkedIn Profile URL : ")
        return info
    else:
        return None


def run(target, lreq=False, output= None):
    dao = data_access_object.DAO()
    dao.main()
    if output is None:
        output = f'{target}.md'
    rpt = p_report.Report("Reports/", output, f"Omniscient Report for {target} \t\t\t")

    l_info = None
    if not lreq:
        l_info = link_parser()
    chain_run(target, rpt, dao)
    if l_info is not None:
        rpt.add_hn(2,'LinkedIn Information [: user submitted :]')
        code, img = p_report.p_dict(l_info)
        rpt.add_cd(code)
