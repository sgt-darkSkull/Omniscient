import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from packages import dao


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Gravatar Profile
    Useful Information on Gravatar Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://en.gravatar.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://en.gravatar.com/{name}"
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
    info['Gravatar_name']= soup.find_all ('a')[7].string
    # Target Gmail
    info['Gravatar_gmail'] = soup.find_all('a')[8].string
    info['Gravatar_link'] = plink
    info['Gravatar_userid'] = name
   
   # not added to the database
    return info


def run(name: str, isurl: bool = False):
    """
    Run Gravatar Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Gravatar', get_info(name, isurl))

if __name__ == '__main__':
    print(run(input()))