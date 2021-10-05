import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Twitter Profile
    Useful Information on facebook Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://www.facebook.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.facebook.com/{name}"
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
    info['name']= soup.find_all ('span')[8].string
    # Target Bio
    info['bio'] = soup.find_all('a')[9].string
    # Target school
    info['school'] = soup.find_all('a')[5].string
    # Target work
    info['work'] = soup.find_all('a')[4].string
    # Target college
    info['college'] = soup.find_all('a')[6].string

    return info
