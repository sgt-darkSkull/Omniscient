from bs4 import BeautifulSoup as BS

from pack_person import dao
import requests


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Freelancer Profile
    Useful Information on Freelancer Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://www.freelancer.com/u/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.freelancer.com/u/{name}"
    else:
        plink = name

    src = requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'
    # Target Real Name
    info['Free_name'] = soup.find_all('h3')[0].string
    # Target Location
    info['Free_location'] = soup.find_all('div')[53].string
    info['Free_link'] = plink
    info['Free_userid'] = name
    dao.update('Users', 'Free_userid', info['Free_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Freelancer Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Freelancer', get_info(name, user_id, isurl), rpt)


if __name__ == '__main__':
    print(get_info('afdafdas', 1, False))
