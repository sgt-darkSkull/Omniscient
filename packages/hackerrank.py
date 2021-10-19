from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Hacker Rank Profile

    Useful Information on Hacker Rank Profile:
        1.  Login Name : userid
        2.  Name: name
        3.  Location: location
        4.  Bio: bio
        5.  LinkedIN ID: lnkid

    Should Look:
        1.  https://www.hackerrank.com/<userid>

    :param name:
    :param isurl:
    :return:
    """

    plink = f"https://www.hackerrank.com/{name}"

    if isurl:
        plink = name

    driver = webdriver.Firefox()
    driver.get(plink)

    src = driver.page_source
    driver.close()
    soup = BS(src, 'html.parser')
    sleep(10)
    info = dict()

    info['name'] = soup.find_all('h1')[0].string
    info['userid'] = soup.find_all('p')[0].string
    info['bio'] = soup.find_all('p')[1].string
    info['location'] = soup.find_all('p')[2].string
    info['lnkid'] = soup.find_all('a', href=True)[8]['href']

    return info


def run(name: str, isurl: bool = False) -> dict:
    """
    Run Hacker Rank Info Check

    :param name:
    :param isurl:
    :return:
    """
    return get_info(name, isurl)


if __name__ == '__main__':
    print(run('AkashMahalik7'))