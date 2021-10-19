import sqlite3
from User import User

conn = sqlite3.connect('Database.sqlite3')
cur = conn.cursor()


def main():
    # Create table
    cur.executescript(

        '''CREATE TABLE IF NOT EXISTS Users
       (User_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        First_Name text, 
        Last_Name text,
        Link_userid text,
        Face_userid text,
        Insta_userid text,
        Git_userid text,
        Hack_userid text,
        Twit_userid text,
        Chef_userid text
        );

        ''')

    cur.executescript(
        '''CREATE TABLE IF NOT EXISTS Linkedin
       (Link_userid text NOT NULL PRIMARY KEY,
        Link_Fname text, 
        Link_Lname text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Facebook
       (Face_userid text NOT NULL PRIMARY KEY,
        Face_Fname text, 
        Face_Lname text,
        Face_School text,
        Face_Collage text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Instagram
       (insta_userid text NOT NULL PRIMARY KEY,
        Insta_Fname text, 
        Insta_Lname text,
        Insta_bio text,
        Insta_Avatar text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Github
       (Git_userid text NOT NULL PRIMARY KEY,
        Git_Fname text, 
        Git_Lname text,
        Git_Location text,
        Git_bio text,
        Git_Company text,
        Git_Email text,
        Git_Blog text,
        Git_Followers text,
        Git_Job_Req text,
        Git_Avatar text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Hackerank
       (Hack_userid text NOT NULL PRIMARY KEY,
        Hack_Fname text, 
        Hack_Lname text,
        Hack_location text,
        Hack_bio text,
        Hack_Institute text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS twitter
       (Twit_userid text NOT NULL PRIMARY KEY,
        Twit_Fname text, 
        Twit_Lname text,
        Twit_location text,
        Twit_bio text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Codechef
       (Chef_userid text NOT NULL PRIMARY KEY,
        Chef_Fname text, 
        Chef_Lname text,
        Chef_location text,
        Chef_bio text,
        Chef_Institute text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );


        ''')

    cur.executescript(
        '''CREATE TABLE IF NOT EXISTS Link_Links
       (Link_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Link_userid text,
        FOREIGN KEY(Link_userid) REFERENCES Linkedin(Link_userid)
        );  

        CREATE TABLE IF NOT EXISTS Face_Links
       (Face_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Face_userid text,
        FOREIGN KEY(Face_Links_id) REFERENCES Face_Links(Face_Links_id)
        ); 

        CREATE TABLE IF NOT EXISTS Insta_Links
       (Insta_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Insta_userid text,
        FOREIGN KEY(Insta_Links_id) REFERENCES Insta_Links(Insta_Links_id)
        ); 

        CREATE TABLE IF NOT EXISTS Git_Links
       (Git_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Git_userid text,
        FOREIGN KEY(Git_Links_id) REFERENCES Git_Links(Git_Links_id)
        ); 

        CREATE TABLE IF NOT EXISTS Hack_Links
       (Hack_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Hack_userid text,
        FOREIGN KEY(Hack_Links_id) REFERENCES Hack_Links(Hack_Links_id)
        ); 

        CREATE TABLE IF NOT EXISTS Twit_Links
       (Twit_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Twit_userid text,
        FOREIGN KEY(Twit_Links_id) REFERENCES Twit_Links(Twit_Links_id)
        ); 

        CREATE TABLE IF NOT EXISTS Chef_Links
       (Chef_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Site text, 
        URL text,
        Chef_userid text,
        FOREIGN KEY(Chef_Links_id) REFERENCES Chef_Links(Chef_Links_id)
        ); 
        ''')


def insert_User(User):
    with conn:
        if (User.First_Name):
            cur.execute('''INSERT INTO Users (First_Name, Last_Name, link_userid, Face_userid, Insta_userid, Git_userid, Hack_userid, Twit_userid, Chef_userid)
                        VALUES (:First_Name, :Last_Name, :link_userid, :Face_userid, :Insta_userid, :Git_userid, :Hack_userid, :Twit_userid, :Chef_userid)''',
                        {'First_Name': User.First_Name, 'Last_Name': User.Last_Name, 'link_userid': User.Link_userid,
                         'Face_userid': User.Face_userid, 'Insta_userid': User.Insta_userid,
                         'Git_userid': User.Git_userid, 'Hack_userid': User.Hack_userid,
                         'Twit_userid': User.Twit_userid, 'Chef_userid': User.Chef_userid})


##USER##
def get_User_by(table, column, value):
    cur.execute("SELECT * FROM :table WHERE :column=:value", {'table': table, 'column': column, 'value': value})
    return cur.fetchall()


def get_Users_data(column, value):
    cur.execute("SELECT * FROM Users WHERE :column=:value", {'column': column, 'value': value})
    return cur.fetchall()


def print_Users_table(table):
    with conn:
        cur.execute(f"SELECT * FROM {table}")
        print(cur.fetchall())


if __name__ == '__main__':
    main()

    User = User('Himanshu', 'Sharma', 'himanshu_otakuu', '', '', '', '', '', '')

    # Insert a User of data
    insert_User(User)

    # get user
    user1 = get_Users_data('Last_Name', 'Sharma')

    # user1=get_User_by('Users','Last_Name','Sharma')

    print(user1)

    print_Users_table('Users');
    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
