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


def editUserProfile(form, username):
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
        error = []
        fname = form['fname']
        lname = form['lname']
        location = form['location']
        newMain = form['add-main']
        oldPass = form['old-pass']
        newPass = form['new-pass']
        confirmPass = form['new-pass-confirm']
        delMain = form['del-main']
        cursor = conn.cursor()
        passwordCursor = conn.cursor()
        if fname:
            # Make sure name is valid
            if len(fname) > 30:
                error.append('Names must be less than 30 characters!')
            # Modify the database
            else:
                modifyFname = ("UPDATE Player SET F_name = '{}' WHERE Username = '{}'".format(fname, username))
                cursor.execute(modifyFname)
        else:
            error.append('First name field must be filled out!')

        if lname:
            # Make sure name is valid
            if len(lname) > 30:
                error.append('Names must be less than 30 characters!')
            # Modify the database
            else:
                modifyLname = ("UPDATE Player SET L_name = '{}' WHERE Username = '{}'".format(lname, username))
                cursor.execute(modifyFname)
        else:
            error.append('Last name field must be filled out!')

        if location:
            # Make sure location is valid
            modifyLocation = ("UPDATE Player SET Location = '{}' WHERE Username = '{}'".format(location, username))
            cursor.execute(modifyFname)
        else:
            error.append('Location field must be filled out!')
            # Modify the database

        if newMain:
            if newMain != "Select an Option"
                addMain = ("INSERT INTO Main_characters (Character_name, Username) VALUES ('{}', '{}')".format(newMain, username))
                cursor.execute(addMain)

        if delMain:
            pass

        if newPass:
            if oldPass:
                if confirmPass == newPass:
                    if len(newPass) >= 6 or len(newPass) <= 36:
                        oldPass = hashlib.sha256(oldPass.encode())
                        modifyPass = ("UPDATE Player SET Password = '{}' WHERE Username = '{}' AND Password = '{}' ".format(newPass, username, oldPass))
                        passwordCursor.execute(modifyPass)
                        for r in passwordCursor:
                            numRows += 1
                            # If the result is anything but one result, it's invalid. Return with errors.
                        if numRows != 1:
                            errors.append('Incorrect password!')
                    else:
                        error.append('New password must be between 6 and 32 characters!')



                else:
                    error.append('Your confimation does not match the new password!')
            else:
                error.append('You must enter your old password!')


        conn.commit()
        cursor.close()
        conn.close()

        return error
