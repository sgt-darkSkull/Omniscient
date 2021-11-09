from bs4 import BeautifulSoup as BS
import requests
from pack_person import data_access_object


def get_info(name: str, user_id: int, isurl: bool, dao) -> dict:
    """
    This Function Filters the User's Coroflot Profile
    Useful Information on Coroflot Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://www.coroflot.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.coroflot.com/{name}"
    else:
        plink = name

    src = requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'
    # Target Real Name
    info['Coro_name'] = soup.find_all('h1')[0].string
    # Target Location
    info['Coro_location'] = soup.find_all('div')[17].string
    info['Coro_link'] = plink
    info['Coro_userid'] = name
    dao.update('Users', 'Coro_userid', info['Coro_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False, dao = None):
    """
    Run Coroflot Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Coroflot', get_info(name, user_id, isurl, dao), rpt)

