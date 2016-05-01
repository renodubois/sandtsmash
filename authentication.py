from bottle import (request, redirect)
from setup import MY_SQL_CONNECTION
import functools
import mysql.connector
import hashlib

'''	requiresLogin
	Function wrapper to require a user to be logged in to access a certain page.
	Accomplishes this by requiring the 'logged_in_as' cookie to be present,
	which is only set when a user logs in successfully.
'''
def requiresLogin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not request.get_cookie('logged_in_as'):
            redirect('/login/')
        else:
            return func(*args, **kwargs)
    return wrapper


def checkLogin(form):
    errors = []
    # Try and connect to the database
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
        # Define a cursor, used to interact with our database.
        cursor = conn.cursor()
        # Grab the username and password that the user entered.
        username = form['username']
        password = form['password']
        # Encrypt the entered password
        # password = hashlib.sha256(password.encode())
        # Sanitize our input.

        # Check to see if the username and password match.
        query = "SELECT * FROM Player WHERE Username ='{}' and Password ='{}'".format(username, password)
        cursor.execute(query)
        numRows = 0
        for r in cursor:
            numRows += 1
        # If the result is anything but one result, it's invalid. Return with errors.
        if numRows != 1:
            errors.append('Invalid username or password!')
        cursor.close()
        conn.close()
        return errors
