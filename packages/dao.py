import sqlite3
from packages.user_dao import User

conn = sqlite3.connect('Database.sqlite3')
cur = conn.cursor()


def main():
    # Create table
    cur.executescript(

        '''CREATE TABLE IF NOT EXISTS Users
       (User_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name text, 
        Link_userid text,
        Face_userid text,
        Insta_userid text,
        Git_userid text,
        Hack_userid text,
        Twit_userid text,
        Chef_userid text,
        Coro_userid text,
        Dev_userid text,
        Ello_userid text,
        Free_userid text,
        Hackaday_userid text,
        Mal_userid text,
        Pink_userid text,
        Reddit_userid text,
        Soundcloud_userid text,
        Typeracer_userid text,
        Ultimate_guitar_userid text,
        Vimeo_userid text,
        Gravatar_userid text
        );

        ''')

    cur.executescript(
        '''CREATE TABLE IF NOT EXISTS Linkedin
       (Link_userid text NOT NULL PRIMARY KEY,
        Link_name text, 
        Link_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Facebook
       (Face_userid text NOT NULL PRIMARY KEY,
        Face_name text, 
        Face_school text,
        Face_collage text,
        Face_work text,
        Face_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Instagram
       (Insta_userid text NOT NULL PRIMARY KEY,
        Insta_name text, 
        Insta_bio text,
        Insta_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Github
       (Git_userid text NOT NULL PRIMARY KEY,
        Git_name text, 
        Git_location text,
        Git_bio text,
        Git_company text,
        Git_email text,
        Git_blog text,
        Git_followers text,
        Git_job_Req text,
        Git_Avatar text,
        Git_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Hackerank
       (Hack_userid text NOT NULL PRIMARY KEY,
        Hack_name text, 
        Hack_location text,
        Hack_bio text,
        Hack_Institute text,
        Hack_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Twitter
       (Twit_userid text NOT NULL PRIMARY KEY,
        Twit_name text, 
        Twit_location text,
        Twit_bio text,
        Twit_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Codechef
       (Chef_userid text NOT NULL PRIMARY KEY,
        Chef_name text, 
        Chef_location text,
        Chef_bio text,
        Chef_Institute text,
        Chef_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Coroflot
       (Coro_userid text NOT NULL PRIMARY KEY,
        Coro_name text, 
        Coro_location text,
        Coro_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Dev_community
       (Dev_userid text NOT NULL PRIMARY KEY,
        Dev_name text, 
        Dev_location text,
        Dev_bio text,
        Dev_skills text,
        Dev_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Ello
       (Ello_userid text NOT NULL PRIMARY KEY,
        Ello_name text, 
        Ello_bio text,
        Ello_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Freelancer
       (Free_userid text NOT NULL PRIMARY KEY,
        Free_name text, 
        Free_location text,
        Free_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Hackaday
       (Hackaday_userid text NOT NULL PRIMARY KEY,
        Hackaday_name text, 
        Hackaday_bio text,
        Hackaday_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Mal
       (Mal_userid text NOT NULL PRIMARY KEY,
        Mal_name text, 
        Mal_gender text,
        Mal_dob text,
        Mal_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Pinkbike
       (Pink_userid text NOT NULL PRIMARY KEY,
        Pink_name text, 
        Pink_location text,
        Pink_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Reddit
       (Reddit_userid text NOT NULL PRIMARY KEY,
        Reddit_name text, 
        Reddit_dob text,
        Reddit_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Soundcloud
       (Soundcloud_userid text NOT NULL PRIMARY KEY,
        Soundcloud_name text, 
        Soundcloud_location text,
        Soundcloud_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Typeracer
       (Typeracer_userid text NOT NULL PRIMARY KEY,
        Typeracer_name text, 
        Typeracer_gender text,
        Typeracer_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

       CREATE TABLE IF NOT EXISTS Ultimate_guitar
       (Guitar_userid text NOT NULL PRIMARY KEY,
        Guitar_name text, 
        Guitar_Dob text,
        Guitar_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Vimeo
       (Vimeo_userid text NOT NULL PRIMARY KEY,
        Vimeo_name text, 
        Vimeo_location text,
        Vimeo_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        CREATE TABLE IF NOT EXISTS Gravatar
       (Gravatar_userid text NOT NULL PRIMARY KEY,
        Gravatar_name text, 
        Gravatar_gmail text,
        Gravatar_link text,
        User_id text,
        FOREIGN KEY(User_id) REFERENCES Users(User_id)
        );

        ''')

    # cur.executescript(
    #     '''CREATE TABLE IF NOT EXISTS Link_Links
    #    (Link_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Link_userid text,
    #     FOREIGN KEY(Link_userid) REFERENCES Linkedin(Link_userid)
    #     );  

    #     CREATE TABLE IF NOT EXISTS Face_Links
    #    (Face_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Face_userid text,
    #     FOREIGN KEY(Face_Links_id) REFERENCES Face_Links(Face_Links_id)
    #     ); 

    #     CREATE TABLE IF NOT EXISTS Insta_Links
    #    (Insta_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Insta_userid text,
    #     FOREIGN KEY(Insta_Links_id) REFERENCES Insta_Links(Insta_Links_id)
    #     ); 

    #     CREATE TABLE IF NOT EXISTS Git_Links
    #    (Git_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Git_userid text,
    #     FOREIGN KEY(Git_Links_id) REFERENCES Git_Links(Git_Links_id)
    #     ); 

    #     CREATE TABLE IF NOT EXISTS Hack_Links
    #    (Hack_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Hack_userid text,
    #     FOREIGN KEY(Hack_Links_id) REFERENCES Hack_Links(Hack_Links_id)
    #     ); 

    #     CREATE TABLE IF NOT EXISTS Twit_Links
    #    (Twit_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Twit_userid text,
    #     FOREIGN KEY(Twit_Links_id) REFERENCES Twit_Links(Twit_Links_id)
    #     ); 

    #     CREATE TABLE IF NOT EXISTS Chef_Links
    #    (Chef_Links_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #     Site text, 
    #     URL text,
    #     Chef_userid text,
    #     FOREIGN KEY(Chef_Links_id) REFERENCES Chef_Links(Chef_Links_id)
    #     ); 
    #     ''')


def insert_User(User):
    with conn:
        if (User.First_Name):
            cur.execute('''INSERT INTO Users (First_Name, Last_Name, link_userid, Face_userid, Insta_userid, Git_userid, Hack_userid, Twit_userid, Chef_userid)
                        VALUES (:First_Name, :Last_Name, :link_userid, :Face_userid, :Insta_userid, :Git_userid, :Hack_userid, :Twit_userid, :Chef_userid)''',
                        {'First_Name': User.First_Name, 'Last_Name': User.Last_Name, 'link_userid': User.Link_userid,
                         'Face_userid': User.Face_userid, 'Insta_userid': User.Insta_userid,
                         'Git_userid': User.Git_userid, 'Hack_userid': User.Hack_userid,
                         'Twit_userid': User.Twit_userid, 'Chef_userid': User.Chef_userid})


def insert(table, dict):
    column = ''
    values = ''
    for key in dict:
        if (dict[key] != ''):
            column += key + ', '
            values += "'" + dict[key] + "'" + ', '
    column = column[:-2]
    values = values[:-2]

    cur.execute(f"INSERT INTO {table} ({column}) VALUES ({values})")


def get(table, column, where_column, where_value):
    cur.execute(f"SELECT {column} FROM {table} WHERE {where_column} = \'{where_value}\'")
    return cur.fetchall()


def update_one(table, change_column, new_value, where_column, where_value):
    cur.execute(f"UPDATE {table} SET {change_column} = \'{new_value}\' WHERE {where_column} = \'{where_value}\'")
    return cur.fetchall()


def update_bulk(table, dict, where_column, where_value):
    str = ''
    for key in dict:
        str += key + "=" + "'" + dict[key] + "'" + ", "

    str = str[:-2]
    print(f"UPDATE {table} SET {str} WHERE {where_column} = \'{where_value}\'")
    cur.execute(f"UPDATE {table} SET {str} WHERE {where_column} = \'{where_value}\'")


def delete(table, where_column, where_value):
    cur.execute(f"DELETE FROM {table} WHERE {where_column} = \'{where_value}\'")
    return cur.fetchall()


if __name__ == '__main__':
    main()

    a_dict = {'First_Name': 'Himanshu', 'Last_Name': '', 'link_userid': '',
              'Face_userid': 'OP player', 'Insta_userid': 'dessNuts',
              'Git_userid': '', 'Hack_userid': 'hs1925846@gamil',
              'Twit_userid': 'yes', 'Chef_userid': 'Yes d', 'free_userid': 'nice'}
    dict2 = {'First_Name': 'Sumit', 'Last_Name': 'ha ha ', 'link_userid': '',
             'Face_userid': 'OPM player', 'Insta_userid': 'suckdessNuts'}
    table = 'Users'
    column = '*'
    change_column = 'Insta_userid'
    new_value = 'Himanshu Otakuu7'
    where_column = 'user_id'
    where_value = '15'

    # insert function
    insert('Users', a_dict)

    # get function
    print(get(table, column, where_column, where_value))

    # update_one function
    update_one(table, change_column, new_value, where_column, where_value)

    # update_bulk
    update_bulk(table, dict2, where_column, where_value)

    # update(table, 'Twit_userid', 'Badiya ek dum', 'Chef_userid', 'Yes d')
    delete(table, 'user_id', '12')

    print(get(table, column, 'user_id', '12'))
    print(get(table, column, 'user_id', '15'))

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
