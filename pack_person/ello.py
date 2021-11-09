from bs4 import BeautifulSoup as BS
from pack_person import data_access_object
import requests


def get_info(name: str, user_id: int, isurl: bool, dao) -> dict:
    """
    This Function Filters the User's Ello Profile
    Useful Information on Ello Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://ello.co/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://ello.co/{name}"
    else:
        plink = name

    src = requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'
    # Target Real Name
    info['Ello_name'] = soup.find_all('a')[0].string
    # Target Bio
    info['Ello_bio'] = soup.find_all('p')[0].string
    info['Ello_link'] = plink
    info['Ello_userid'] = name
    dao.update('Users', 'Ello_userid', info['Ello_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False, dao = None):
    """
    Run Ello Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Ello', get_info(name, user_id, isurl, dao), rpt)
