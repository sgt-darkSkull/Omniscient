import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import dao
import requests



def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Pinkbike Profile
    Useful Information on Pinkbike Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://www.pinkbike.com/u/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.pinkbike.com/u/{name}/"
    else:
        plink = name

    src=requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return'NODATARETURNED'

    
    # Target Real Name
    info['Pink_name']= soup.find_all ('h1')[0].string
    # Target Location
    info['Pink_location'] = soup.find_all('li')[33].string
    info['Pink_link'] = plink
    info['Pink_userid'] = name
    dao.update('Users', 'Pink_userid', info['Pink_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, isurl: bool = False):
    """
    Run Pinkbike Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Pinkbike', get_info(name, user_id, isurl))

if __name__ == '__main__':
    print(get_info('adfafag', 1, False))
    # print(run(input()))