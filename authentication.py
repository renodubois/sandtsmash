from bottle import (request, redirect)
import functools
import mysql.connector

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


def validateForm(form):
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
	    userLength = len(form['username'])
	    passLength = len(form['password'])
	    if not form['username']:
		    # Error; username can't be blank
		    print('poo')
	    elif not form['password']:
		    # Error; password can't be blank
		    print('more poo')
	    # Sanitize input, then check database for match.
	    else:
            cursor = conn.cursor()
            # Encrypt the entered password
            password = hashlib.sha256(password.encode())
            # Check to see if the username and password match.
            query = "SELECT * FROM users WHERE username ='{}' and password ='{}'".format(username, password.hexdigest())
            cursor.execute(query)
            for r in cursor:
		        print(r)
            cursor.close()
            conn.close()
