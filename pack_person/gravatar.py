from bs4 import BeautifulSoup as BS
from pack_person import dao
import requests


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Gravatar Profile
    Useful Information on Gravatar Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://en.gravatar.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://en.gravatar.com/{name}"
    else:
        plink = name

    src = requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'
    # Target Real Name
    info['Gravatar_name'] = soup.find_all('a')[7].string
    # Target Gmail
    info['Gravatar_gmail'] = soup.find_all('a')[8].string
    info['Gravatar_link'] = plink
    info['Gravatar_userid'] = name

    dao.update('Users', 'Gravatar_userid', info['Gravatar_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Gravatar Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Gravatar', get_info(name, user_id, isurl), rpt)
