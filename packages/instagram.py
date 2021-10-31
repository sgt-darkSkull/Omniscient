import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from packages import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Instagram Profile
    Useful Information on Github Profile:
        1.  Login Name : userid
        2.  Name: name
        3. Bio: bio
    Should Look:
        1.  https://instagram.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://instagram.com/{name}"
    else:
        plink = name

    # Firefox Driver (Selenium)
    driver = webdriver.Firefox()
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    driver.close()

    # Target Real Name
    info['Insta_name'] = driver.find_element_by_class_name('rhpdm').string
    # Target User ID
    info['Insta_userid'] = driver.find_element_by_class_name('_7UhW9       fKFbl yUEEX   KV-D4              fDxYl  ').string
    # Target Bio
    info['Insta_bio'] = driver.find_element_by_class_name('-vDIg').string
    info['Insta_link'] = plink
    info['Insta_userid'] = name
    dao.update('Users', 'Insta_userid', info['Insta_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, isurl: bool = False):
    """
    Run Twitter Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Instagram', get_info(name, user_id, isurl))


if __name__ == '__main__':
    print(get_info(input()))