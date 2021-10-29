import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def get_info(name: str, isurl: bool) -> dict:
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

    # Firefox Driver (Selenium)
    driver = webdriver.chrome()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()
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
   
    return info


def run(name: str, isurl: bool = False) -> dict:
    """
    Run Dev_Community Info Check
    :param isurl:
    :param name:
    :return:
    """
    return get_info(name, isurl)


if __name__ == '__main__':
    print(run(input()))