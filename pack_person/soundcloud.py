import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from webdriver_manager.chrome import ChromeDriverManager
from pack_person import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Soundcloud Profile
    Useful Information on Soundcloud Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://soundcloud.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://soundcloud.com/{name}"
    else:
        plink = name

    # Firefox Driver (Selenium)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(plink)

    # Approx Wait ( high speed internet required)
    time.sleep(15)  # 15 Seconds Sleep

    # Parsing HTML Source code to Extract Information
    soup = BS(driver.page_source, 'html.parser')
    driver.close()

    title = soup.find('title').string
    
    
    if name.lower() not in title.lower():
        return'NODATARETURNED'
        
    # Target Real Name
    info['Soundcloud_name']= soup.find_all ('h2')[0].string
    # Target Location
    info['Soundcloud_location'] = soup.find_all('h3')[1].string
    info['Soundcloud_link'] = plink
    info['Soundcloud_userid'] = name
    dao.update('Users', 'Soundcloud_userid', info['Soundcloud_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Soundcloud Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Soundcloud', get_info(name, user_id, isurl), rpt)

if __name__ == '__main__':
    print(get_info('afdagvbafd', 1, False))
    # print(run(input()))