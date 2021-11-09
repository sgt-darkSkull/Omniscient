from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep
from pack_person import data_access_object


def get_info(name: str, user_id: int, isurl: bool, dao) -> dict:
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
    sleep(15)  # 15 Seconds Sleep

    src = driver.page_source
    driver.quit()

    soup = BS(src, 'html.parser')
    sleep(10)
    info = dict()

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'

    # Target Real Name
    info['Insta_name'] = soup.find_all('h1')[0].string
    # Target User ID
    info['Insta_userid'] = name
    # Target Bio
    info['Insta_bio'] = soup.find_all('span')[3].string
    info['Insta_link'] = plink
    info['Insta_userid'] = name
    import instaloader, sys, os

    sys.stdout = open(os.devnull, 'w')
    mod=instaloader.Instaloader()
    mod.download_profile(name, profile_pic_only=True)
    sys.stdout = sys.__stdout__

    if os.path.isdir(name):
        for file in os.listdir(name):
            if ('.jpg' or '.png') in file:
                info['Insta_DP'] = file
                with open(name+'/' + file,'rb') as fp:
                    outf = open(file,'wb')
                    outf.write(fp.read())
                import shutil
                shutil.rmtree(name)



    dao.update('Users', 'Insta_userid', info['Insta_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False, dao = None):
    """
    Run Twitter Info Check
    :param isurl:
    :param name:
    :return:
    """
    dao.insert('Instagram', get_info(name, user_id, isurl, dao), rpt)
