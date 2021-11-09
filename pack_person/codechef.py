import requests
from bs4 import BeautifulSoup as BS

from pack_person import dao


def get_info(name: str, user_id: int, isurl: bool) -> dict:
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

    title = soup.find('title').string

    if name.lower() not in title.lower():
        return 'NODATARETURNED'

    info = dict()

    tag_span = soup.find_all('span')
    info['Chef_userid'] = tag_span[5].string
    info['Chef_name'] = tag_span[5].string
    info['Chef_location'] = tag_span[9].string + ', ' + \
                            tag_span[8].string + ', ' + tag_span[7].string
    info['Chef_institute'] = tag_span[10].string
    info['Chef_link'] = plink
    dao.update('Users', 'Chef_userid', info['Chef_userid'], 'User_id', user_id)
    return info


def run(name: str, user_id: int, rpt, isurl: bool = False):
    """
    Run Code Chef Info Check

    :param name:
    :param isurl:
    :return:
    """
    dao.insert('Codechef', get_info(name, user_id, isurl), rpt)


if __name__ == '__main__':
    # print(get_info('stromprod', 1, False))
    dao.insert('Codechef', get_info('stromprod', 1, False))

    # print(run('afdhasfdl'))
