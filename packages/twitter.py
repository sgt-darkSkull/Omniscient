import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def get_info(name: str) -> dict:

    """
    This Function Filters the User's Twitter Profile

    Useful Information on Github Profile:
        1.  Login Name : userid
        2.  Name: name
        3.  Location: location
        4. Bio: bio

    Should Look:
        1.  https://twitter.com/<userid>

    :param name:
    :return info:
    """

    info = dict()
    plink = f"https://twitter.com/{name}"

    # Firefox Driver (Selenium)
    driver = webdriver.Firefox()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()

    # Target Real Name
    info['name'] = soup.find_all('span')[17].string
    # Target User ID
    info['userid'] = soup.find_all('span')[25].string
    # Target Bio
    info['bio'] = soup.find_all('span')[26].string
    # Target Location
    info['location'] = soup.find_all('span')[28].string

    return info


if __name__ == '__main__':
    print(get_info(input()))
