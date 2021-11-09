import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from pack_person import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Ultimate-guitar Profile
    Useful Information on Ultimate-guitar Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://www.ultimate-guitar.com/u/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.ultimate-guitar.com/u/{name}"
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
    info['Guitar_name'] = soup.find_all('h1')[0].string
    # Target Birthday
    info['Guitar_dob'] = soup.find_all('div')[57].string
    info['Guitar_link'] = plink
    info['Guitar_userid'] = name
    dao.update('Users', 'Guitar_userid', info['Guitar_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Ultimate-guitar Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Ultimate_guitar', get_info(name, user_id, isurl), rpt)
