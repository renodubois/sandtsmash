import mysql.connector

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
        cursor = conn.cursor()
        query = "SELECT * FROM Player WHERE Username='{}'".format(username)
        cursor.execute(query)
        for result in cursor:
            print(result)

        cursor.close()
        conn.close()
