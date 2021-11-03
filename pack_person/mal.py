import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS

from pack_person import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
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

    src = driver.page_source
    driver.close()


    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()

    title = soup.find('title').string
    
    if name not in title.lower():
        return'NODATARETURNED'

    # Target Real Name
    info['Mal_name']= soup.find_all ('h1')[0].string
    # Target Gender
    info['Mal_gender'] = soup.find_all('span')[8].string
    # Target Birthday
    info['Mal_dob'] = soup.find_all('span')[10].string
    info['Mal_link'] = plink
    info['Mal_userid'] = name
    dao.update('Users', 'Mal_userid', info['Mal_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, isurl: bool = False):
    """
    Run Mal Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Mal', get_info(name, user_id, isurl))

if __name__ == '__main__':
    # print(get_info('himanshu_otakuu', 1, False))
    print(run(input()))