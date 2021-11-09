from bs4 import BeautifulSoup as BS

import requests


def get_info(name: str, user_id: int, isurl: bool) -> dict:
    """
    This Function Filters the User's Flickr Profile
    Useful Information on Flickr Profile:
        1.  Work: work
        2.  Name: name
        3.  College: college
        4.  Bio: bio
        5.  School: school
    Should Look:
        1.  https://www.flickr.com/people/<userid>
    :param isurl:
    :param name:
    :return info:
    """

    info = dict()
    if not isurl:
        plink = f"https://www.flickr.com/people/{name}"
    else:
        plink = name

    src = requests.get(plink).content

    # Parsing HTML Source code to Extract Information
    soup = BS(src, 'html.parser')

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'
    # Target Real Name
    info['name'] = soup.find_all('h1')[0].string
    # Target Occupation
    info['occupation'] = soup.find_all('span')[18].string
    # Target Hometown
    info['hometown'] = soup.find_all('span')[20].string
    # Target Current City
    info['city'] = soup.find_all('span')[22].string
    # Target Country
    info['Country'] = soup.find_all('span')[24].string
    # Target Bio
    info['Bio'] = soup.find_all('span')[13].string

    # not added in database

    return info


def run(name: str, user_id: int, isurl: bool = False) -> dict:
    """
    Run Flickr Info Check
    :param isurl:
    :param name:
    :return:
    """
    return get_info(name, user_id, isurl)
