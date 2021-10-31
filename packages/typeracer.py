import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from packages import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Typeracer Profile
    Useful Information on Typeracer Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://data.typeracer.com/pit/profile?user=<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://data.typeracer.com/pit/profile?user={name}"
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
    info['Typeracer_name']= soup.find_all ('td')[27].string
    # Target Gender
    info['Typeracer_gender'] = soup.find_all('td')[29].string
    info['Typeracer_link'] = plink
    info['Typeracer_userid'] = name
    dao.update('Users', 'Typeracer_userid', info['Typeracer_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, isurl: bool = False):
    """
    Run Typeracer Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Typeracer', get_info(name, user_id, isurl))

if __name__ == '__main__':
    print(run(input()))