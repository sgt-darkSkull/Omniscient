import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from packages import dao


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Facebook Profile
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
    info['Face_name']= soup.find_all ('span')[8].string
    # Target Bio
    info['Face_bio'] = soup.find_all('a')[9].string
    # Target school
    info['Face_school'] = soup.find_all('a')[5].string
    # Target work
    info['Face_work'] = soup.find_all('a')[4].string
    # Target college
    info['Face_college'] = soup.find_all('a')[6].string
    info['Face_link'] = plink
    info['Face_userid'] = name

    return info


def run(name: str, isurl: bool = False):
    """
    Run Facebook Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert("Facebook", get_info(name, isurl))


if __name__ == '__main__':
    print(run(input()))