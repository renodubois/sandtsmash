import mysql.connector
from setup import MY_SQL_CONNECTION

def updateCurUsers():
    try:
        conn = mysql.connector.connect(user=MY_SQL_CONNECTION[0],
        password=MY_SQL_CONNECTION[1], host=MY_SQL_CONNECTION[2],
        database=MY_SQL_CONNECTION[3])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong w/ username and password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Test database doesn\'t exist')
        else:
            print(err)
    else:
        users = []
        cursor = conn.cursor()
        query = "SELECT Username FROM Player"
        cursor.execute(query)
        for r in cursor:
            print(r)
            users.append(r[0])
        cursor.close()
        conn.close()
        return users

def retrieveUserInfo(username):
    # Takes a username, and returns a dict with info related to that user.
    try:
        conn = mysql.connector.connect(user=MY_SQL_CONNECTION[0],
        password=MY_SQL_CONNECTION[1], host=MY_SQL_CONNECTION[2],
        database=MY_SQL_CONNECTION[3])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong w/ username and password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Test database doesn\'t exist')
        else:
            print(err)
    else:
        userInfo = {}
        cursor = conn.cursor()
        query = "SELECT * FROM Player WHERE Username='{}'".format(username)
        cursor.execute(query)
        for result in cursor:
            userInfo['fname'] = result[2]
            userInfo['lname'] = result[3]
            userInfo['location'] = result[4]
            if result[5]:
                userInfo['ranking'] = result[5]

        cursor.close()
        conn.close()
        return userInfo
