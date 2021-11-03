import json
import requests
from pack_person import dao
# import dao

# [-] INCOMPLETE : PARSING FOR IF VALUE EXIST
# [-] INCOMPLETE : AI IMAGE RECOGNITION

# Profile API : https://api.github.com/users/<username>
# Repos API : https://api.github.com/users/<username>/repos
# Event API : https://api.github.com/users/<username>/events/public
# avatar_url	"https://avatars.githubusercontent.com/u/<user-id>"
# avatar_url	"https://avatars.githubusercontent.com/u/<user-id>"
# url	"https://api.github.com/users/<username>"
# html_url	"https://github.com/<username>"
# followers_url	"https://api.github.com/users/<username>/followers"
# following_url	"https://api.github.com/users/<username>/following{/other_user}"
# gists_url	"https://api.github.com/users/<username>/gists{/gist_id}"
# starred_url	"https://api.github.com/users/<username>/starred{/owner}{/repo}"
# subscriptions_url	"https://api.github.com/users/<username>/subscriptions"
# organizations_url	"https://api.github.com/users/<username>/orgs"
# repos_url	"https://api.github.com/users/<username>/repos"
# events_url	"https://api.github.com/users/<username>/events{/privacy}"
# received_events_url	"https://api.github.com/users/<username>/received_events"


def value_of(value: str):
    if value == '""' or value is None:
        return False
    else:
        return value


# User Profile Info Gatherer
def get_userinfo(name: str, user_id: int) -> dict:
    # https: // api.github.com / users / < username >

    """
    This Function Filters the User's Github Profile

    Useful Information on Github Profile:
        1.  Login Name : login
        2.  User Github ID: id
        3.  Avatar : avatar_url
        4.  Following : following_url
        5.  Name: name
        6.  Company: company
        7.  Blog:   blog
        8.  Location: location
        9.  Email: email
        10. Job Req: hireable
        11. Bio: bio
        12. Twitter: twitter_username

    Should Look:
        1.  https://api.github.com/users/<username>/followers
        2.  https://api.github.com/users/<username>/subscriptions
        3.  https://api.github.com/users/<username>/events

    :param name:
    :return info:
    """

    call_url = f"https://api.github.com/users/{name}"
    rq = requests.get(call_url)
    if rq.status_code != 200:
        return None

    js_obj = json.loads(rq.content.decode('utf-8'))

    info = dict()

    prstr = f'''
        1.  Login Name : {js_obj['login']}
        2.  User Github ID: {js_obj['id']}
        3.  Avatar : {js_obj['avatar_url']}
        4.  Following : {get_following(name)}
        5.  Name: {js_obj['name']}
        6.  Company: {js_obj['company']}
        7.  Blog:   {js_obj['blog']}
        8.  Location: {js_obj['location']}
        9.  Email: {js_obj['email']}
        10. Job Req: {js_obj['hireable']}
        11. Bio: {js_obj['bio']}
        12. Twitter: {js_obj['twitter_username']}

    Should Look
        1.  https://api.github.com/users/{js_obj['login']}/followers
        2.  https://api.github.com/users/{js_obj['login']}/subscriptions
        3.  https://api.github.com/users/{js_obj['login']}/events'''

    for key in js_obj:
        info[key] = js_obj[key] if value_of(js_obj[key]) else None
    info['Git_link'] = call_url
    dao.update('Users', 'id', info['id'], 'User_id', user_id)
    return info


# Get Followed Users
def get_following(name: str) -> list:
    url = f"https://api.github.com/users/{name}/following"

    js_obj = json.loads(requests.get(url).content.decode('utf-8'))
    following = list()

    for folw in js_obj:
        following.append(folw['login'])

    return following


def run(name: str, user_id: int):
    """
    Run Github Info Check

    :param name:
    :return:
    """
    # return get_userinfo(name)
    dao.insert('Github', get_userinfo(name, user_id))


if __name__ == '__main__':
    print(run('amarnath-arch'))
