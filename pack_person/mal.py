from bs4 import BeautifulSoup as BS
from pack_person import dao
import requests


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Mal Profile
    Useful Information on Mal Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://myanimelist.net/profile/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://myanimelist.net/profile/{name}"
    else:
        plink = name

    src = requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'

    title = soup.find('title').string

    if name not in title.lower():
        return 'NODATARETURNED'

    # Target Real Name
    info['Mal_name'] = soup.find_all('h1')[0].string
    # Target Gender
    info['Mal_gender'] = soup.find_all('span')[8].string
    # Target Birthday
    info['Mal_dob'] = soup.find_all('span')[10].string
    info['Mal_link'] = plink
    info['Mal_userid'] = name
    dao.update('Users', 'Mal_userid', info['Mal_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Mal Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Mal', get_info(name, user_id, isurl), rpt)
