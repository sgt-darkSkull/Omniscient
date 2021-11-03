import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Newgrounds Profile
    Useful Information on Newgrounds Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://david.newgrounds.com/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://david.newgrounds.com/{name}"
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

    title = soup.find('title').string
    
    if name not in title.lower():
        return'NODATARETURNED'
        
    # Target Real Name
    info['name']= soup.find_all ('a')[4].string
    # Target Gender/Age
    info['gender_age'] = soup.find_all('span')[0].string
    # Target Location
    info['location'] = soup.find_all('span')[2].string
   
   #not added in the database (gender_age)
    return info


def run(name: str, user_id: int, isurl: bool = False) -> dict:
    """
    Run Newgrounds Info Check
    :param isurl:
    :param name:
    :return:
    """
    return get_info(name, user_id, isurl)


if __name__ == '__main__':
    print(run(input()))