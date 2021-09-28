from packages import github
from packages import twitter

if __name__ == '__main__':

    name = "stamparm"

    gitinfo = github.run(name)
    twitterinfo = twitter.run(gitinfo['blog'], True)

    print(gitinfo)
    print(twitterinfo)