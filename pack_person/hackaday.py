import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from pack_person import dao
import requests


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Hackaday Profile
    Useful Information on Hackaday Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://hackaday.io/David<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://hackaday.io/{name}"
    else:
        plink = name

    src=requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return'NODATARETURNED'
    # Target Real Name
    info['Hackaday_name'] = soup.find_all('h1')[0].string
    # Target Bio
    info['Hackaday_bio'] = soup.find_all('p')[0].string
    info['Hackaday_link'] = plink
    info['Hackaday_userid'] = name
    dao.update('Users', 'Hackaday_userid', info['Hackaday_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Hackaday Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Hackaday', get_info(name, user_id, isurl), rpt)

if __name__ == '__main__':
    print(get_info('afdagbvsadf', 1, False))
    
