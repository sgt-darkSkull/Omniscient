import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def get_info(name: str, isurl: bool) -> dict:
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
    driver = webdriver.chrome()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()
    # Target Real Name
    info['Vimeo_name']= soup.find_all ('div')[191].string
    # Target Location
    info['Vimeo_location'] = soup.find_all('div')[192].string
    info['Vimeo_link'] = plink
    info['Vimeo_userid'] = name
   
    return info


def run(name: str, isurl: bool = False) -> dict:
    """
    Run Vimeo Info Check
    :param isurl:
    :param name:
    :return:
    """
    return get_info(name, isurl)


if __name__ == '__main__':
    print(run(input()))