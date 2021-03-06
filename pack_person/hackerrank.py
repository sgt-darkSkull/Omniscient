from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep

from pack_person import data_access_object


def get_info(name: str, user_id: int, isurl: bool, dao):
    """
    This Function Filters the User's Hacker Rank Profile

    Useful Information on Hacker Rank Profile:
        1.  Login Name : userid
        2.  Name: name
        3.  Location: location
        4.  Bio: bio
        5.  LinkedIN ID: lnkid

    Should Look:
        1.  https://www.hackerrank.com/<userid>

    :param name:
    :param isurl:
    :return:
    """

    plink = f"https://www.hackerrank.com/{name}"

    if isurl:
        plink = name

    driver = webdriver.Firefox()
    driver.get(plink)

    src = driver.page_source
    driver.close()

    if 'page not found' in src.lower():
        return 'NODATARETURNED'

    soup = BS(src, 'html.parser')
    sleep(10)
    info = dict()

    info['Hack_name'] = soup.find_all('h1')[0].string
    info['Hack_userid'] = name  # soup.find_all('p')[0].string
    info['Hack_bio'] = soup.find_all('p')[1].string
    info['Hack_location'] = soup.find_all('p')[2].string
    # info['Hack_lnkid'] = soup.find_all('a', href=True)[8]['href']
    info['Hack_link'] = plink
    dao.update('Users', 'Hack_userid', info['Hack_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False, dao = None):
    """
    Run Hacker Rank Info Check

    :param name:
    :param isurl:
    :return:
    """
    dao.insert('Hackerrank', get_info(name, user_id, isurl, dao), rpt)
