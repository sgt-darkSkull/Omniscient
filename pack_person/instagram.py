from selenium import webdriver
from bs4 import BeautifulSoup as BS
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from pack_person import dao


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
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    sleep(15)  # 15 Seconds Sleep

    src = driver.page_source
    driver.quit()

    soup = BS(src, 'html.parser')
    sleep(10)
    info = dict()

    title = soup.find('title').string
    
    if name.lower() not in title.lower():
        return'NODATARETURNED'

    # Target Real Name
    info['Insta_name'] = soup.find_all('h1')[0].string
    # Target User ID
    info['Insta_userid'] = name
    # Target Bio
    info['Insta_bio'] = soup.find_all('span')[1].string
    info['Insta_link'] = plink
    info['Insta_userid'] = name
    
    dao.update('Users', 'Insta_userid', info['Insta_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Twitter Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Instagram', get_info(name, user_id, isurl), rpt)


if __name__ == '__main__':
    # print(get_info('himanshu_otakuu',1, False))
    dao.insert('Instagram', get_info('gasfdsb',1, False))
    # print(get_info(input()))