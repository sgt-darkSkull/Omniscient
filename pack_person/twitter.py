import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from pack_person import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Twitter Profile

    Useful Information on Twitter Profile:
        1.  Login Name : userid
        2.  Name: name
        3.  Location: location
        4.  Bio: bio

    Should Look:
        1.  https://twitter.com/<userid>

    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://twitter.com/{name}"
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
    
    title = soup.find('title')
    
    if name not in title.lower():
        return'NODATARETURNED'
        
    # Target Real Name
    info['Twit_name'] = soup.find_all('span')[17].string
    # Target User ID
    info['Twit_userid'] = soup.find_all('span')[25].string
    # Target Bio
    info['Twit_bio'] = soup.find_all('span')[26].string
    # Target Location
    info['Twit_location'] = soup.find_all('span')[28].string
    info['Twit_link'] = plink
    dao.update('Users', 'Twit_userid', info['Twit_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, isurl: bool = False):
    """
    Run Twitter Info Check

    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Twitter', get_info(name, user_id, isurl))

if __name__ == '__main__':
    print(run(input()))
