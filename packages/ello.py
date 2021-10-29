import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from packages import dao


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Ello Profile
    Useful Information on Ello Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://ello.co/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://ello.co/{name}"
    else:
        plink = name

    # Firefox Driver (Selenium)
    driver = webdriver.chrome()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()
    # Target Real Name
    info['Ello_name']= soup.find_all ('a')[0].string
    # Target Bio
    info['Ello_bio'] = soup.find_all('p')[0].string
    info['Ello_link'] = plink
    info['Ello_userid'] = name
   
    return info


def run(name: str, isurl: bool = False):
    """
    Run Ello Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Ello', get_info(name, isurl))

if __name__ == '__main__':
    print(run(input()))