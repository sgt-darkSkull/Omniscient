import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Mal Profile
    Useful Information on Mal Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://myanimelist.net/profile/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://myanimelist.net/profile/{name}"
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
    info['Mal_name']= soup.find_all ('h1')[0].string
    # Target Gender
    info['Mal_gender'] = soup.find_all('span')[8].string
    # Target Birthday
    info['Mal_dob'] = soup.find_all('span')[10].string
    info['Mal_link'] = plink
    info['Mal_userid'] = name
   
    return info


def run(name: str, isurl: bool = False) -> dict:
    """
    Run Mal Info Check
    :param isurl:
    :param name:
    :return:
    """
    return get_info(name, isurl)


if __name__ == '__main__':
    print(run(input()))