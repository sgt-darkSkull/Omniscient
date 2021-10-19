import requests
from bs4 import BeautifulSoup as BS


def get_info(name: str, isurl: bool) -> dict:
    """
    This Function Filters the User's Code Chef Profile

    Useful Information on Hacker Rank Profile:
        1.  Login Name : userid
        2.  Name: name
        3.  Location: location
        4.  Bio: bio
        5.  LinkedIN ID: lnkid

    Should Look:
        1.  https://www.codechef.com/users/<userid>

    :param name:
    :param isurl:
    :return:
    """

    plink = f"https://www.codechef.com/users/{name}"

    if isurl:
        plink = name

    src = requests.get(plink).content
    soup = BS(src, 'html.parser')
    info = dict()

    tag_span = soup.find_all('span')
    info['userid'] = tag_span[5].string
    info['location'] = tag_span[9].string+', '+tag_span[8].string+', '+tag_span[7].string
    info['institute'] = tag_span[10].string

    return info


def run(name: str, isurl: bool = False) -> dict:
    """
    Run Code Chef Info Check

    :param name:
    :param isurl:
    :return:
    """
    return get_info(name, isurl)


if __name__ == '__main__':
    print(run('stormprod'))