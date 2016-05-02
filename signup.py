from setup import MY_SQL_CONNECTION
import mysql.connector


def formValidation(form):
    #Import all of the form information into variables
    username = form['username']
    fname = form['fname']
    lname = form['lname']
    location = form['location']
    password = form['password']
    password_confirm = form['password-confirm']
    #Create list to hold all the errors
    error = []
    if len(username) < 4 or len(username) > 20:
        error.append('Username must be between 4 and 20 characters!')
    if fname == '':
        error.append('First name field must be filled out!')
    if len(fname) > 30:
        error.append('Names must be less than 30 characters!')
    if lname == '':
        error.append('Last name field must be filled out!')
    if len(lname) > 30:
        error.append('Names must be less than 30 characters!')
    if location == '':
        error.append('Location field must be filled out!')
    if len(password) < 6 or len(password) > 36:
        error.append('Password must be between 6 and 36 characters!')
    if password != password_confirm:
        error.append('Password does not match confirmation password!')

    return error


def formInsertion(form):
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
        #Import all of the form information into variables
        username = form['username']
        fname = form['fname']
        lname = form['lname']
        location = form['location']
        password = form['password']

        addPlayer = ('INSERT INTO Player '
                    '(Username, Password, F_name, L_name, Location) '
                    'VALUES ({}, {}, {}, {}, {})'.format(username, fname, lname, location, password))
        #Insert new Player into the Database
        cursor.execute(addPlayer)
