class User:
    """A sample Employee class"""

    def __init__(self, First_Name, Last_Name, Link_userid, Face_userid, Insta_userid, Git_userid, Hack_user, Twit_userid, Chef_userid):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Link_userid = Link_userid
        self.Face_userid  = Face_userid
        self.Insta_userid = Insta_userid
        self.Git_userid = Git_userid
        self.Hack_userid = Hack_user
        self.Twit_userid = Twit_userid
        self.Chef_userid = Chef_userid


    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.First_Name, self.Last_Name, self.Link_userid, self.Face_userid, self.Insta_userid, self.Git_userid, self.Hack_userid, self.Twit_userid, self.Chef_userid)
