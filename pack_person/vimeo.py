import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from pack_person import data_access_object


def get_info(name: str, user_id: int, isurl: bool, dao) -> dict:
    """
    This Function Filters the User's Vimeo Profile
    Useful Information on Vimeo Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://vimeo.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://vimeo.com/{name}"
    else:
        plink = name

    # Firefox Driver (Selenium)
    driver = webdriver.Firefox()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'

    # Target Real Name
    info['Vimeo_name'] = soup.find_all('div')[191].string
    # Target Location
    info['Vimeo_location'] = soup.find_all('div')[192].string
    info['Vimeo_link'] = plink
    info['Vimeo_userid'] = name
    dao.update('Users', 'Vimeo_userid', info['Vimeo_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False, dao = None):
    """
    Run Vimeo Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Vimeo', get_info(name, user_id, isurl, dao), rpt)
