import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from pack_person import data_access_object


def get_info(name: str, user_id: int, isurl: bool, dao) -> dict:
    """
    This Function Filters the User's Reddit Profile
    Useful Information on Reddit Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://https://www.reddit.com/user/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.reddit.com/user/{name}"
    else:
        plink = name

    # Firefox Driver (Selenium)
    driver = webdriver.Firefox()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.quit()

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'
    # Target Real Name
    info['Reddit_name'] = soup.find_all('a')[82].string
    # Target Birthday
    info['Reddit_dob'] = soup.find_all('span')[89].string
    info['Reddit_link'] = plink
    info['Reddit_userid'] = name
    dao.update('Users', 'Reddit_userid', info['Reddit_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False, dao = None):
    """
    Run Reddit Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Reddit', get_info(name, user_id, isurl, dao), rpt)
