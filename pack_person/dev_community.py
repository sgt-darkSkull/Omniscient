import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

import dao
import requests


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Dev_Community Profile
    Useful Information on Dev_Community Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://dev.to/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://dev.to/{name}"
    else:
        plink = name
        
        
    src=requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return'NODATARETURNED'
    
    # Target Real Name
    info['Dev_name']= soup.find_all ('h1')[0].string
    # Target Location
    info['Dev_location'] = soup.find_all('span')[14].string
    # Target Skills
    info['Dev_skills'] = soup.find_all('p')[12].string
    # Target Github
    # info['Dev_git'] = soup.find_all('a')[28].string
    # Target Bio
    info['Dev_bio'] = soup.find_all('p')[8].string
    info['Dev_link'] = plink
    info['Dev_userid'] = name
    dao.update('Users', 'Dev_userid', info['Dev_userid'], 'User_id', user_id)

    return info


def run(name: str, user_id: int, isurl: bool = False):
    """
    Run Dev_Community Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Dev_community', get_info(name, user_id, isurl))

if __name__ == '__main__':
    # print(run(input()))
    print(get_info('David', 1, False))
    