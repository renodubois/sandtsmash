from setup import MY_SQL_CONNECTION
import mysql.connector
import datetime

def getCurrentEvents(username):
    '''
    getCurrentEvents()
    Desc: Looks through our SQL database, grabs events that haven't happened yet,
    and returns their info in dicts.
    Returns: a list, collectedEvents, that contains dicts that have event info.
    '''
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
        # Cursor to run querys.
        cursor = conn.cursor()
        # Dictionary used to hold event details.
        eventInfo = {}
        # Current time, used to find out if our events have happened yet or not.
        curTime = datetime.datetime.today()
        # Format used to convert SQL Datetime to Python's datetime
        dateFormat = '%Y-%m-%d %H:%M:%S'
        # The list of dicts that we'll be returning.
        collectedEvents = []
        cursor.execute("SELECT * FROM Event")

        for r in cursor:
            eventInfo = {}
            eventTime = r[1]  #datetime.datetime.strptime(r[1], dateFormat)
            # Only grab events that have not happened yet.
            if eventTime > curTime:
                eventInfo['id'] = r[0]
                eventInfo['eventDate'] = r[1].strftime("%B, %d %Y")  # datetime.datetime.strptime(r[1], dateFormat)
                eventInfo['eventTime'] = r[1].strftime("%I:%M %p")
                eventInfo['entryfee'] = float(r[2])
                eventInfo['maxPlayers'] = r[3]
                eventInfo['location'] = r[4]
                eventInfo['name'] = r[7]
                eventInfo['attendees'] = findCompetitors(r[0])
                eventInfo['numAttendees'] = len(findCompetitors(r[0]))
                if username:
                    eventInfo['userRegistered'] = userInEvent(r[0], username)
                else:
                    pass
                collectedEvents.append(eventInfo)
        return collectedEvents

def findCompetitors(eventId):
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
        attendees = []
        cursor.execute("SELECT Username FROM Competes_in WHERE Event_id = '{}'".format(eventId))
        for r in cursor:
            attendees.append(r)
        return attendees

def getFinishedEvents():
    pass

def eventValidation(form):
    #Import all of the form information into variables
    dateFormat = '%Y-%m-%d %H:%M:%S %p'
#event_id = form['event_id']
    event_date = datetime.datetime.strptime(form['event_date'], dateFormat) 
    entry_fee = form['entry_fee']
    max_participants = form['max_participants']
    location = form['location']
    is_streaming = form['is_streaming']
    provides_stream = form['provides_stream']
    event_name = form['event_name']
    #Create list to hold all the errors
    error = []
#if event_id == '':
#       pass
#       error.append('')
    #if type(event_date) is datetime
    if event_date == '':
        error.append('Event date field must be filled out!')
    if event_date <= datetime.datetime.today():
        error.append('The date/time cannot already have passed!')
    if max_participants == '':
        error.append('You must have a maximum number of participants!')
    if location == '':
        error.append('Location field must be filled out!')
    return error

def eventInsertion(form):
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
        event_date = form['event_date']
        entry_fee = form['entry_fee']
        max_participants = form['max_participants']
        location = form['location']
        is_streaming = form['is_streaming']
        provides_stream = form['provides_stream']
        event_name = form['event_name']
        #game = form['game']

        addEvent = ("INSERT INTO Event (Event_date, Entry_fee, Max_participants, Location, Is_streaming, Provides_stream, Name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(event_date, entry_fee, max_participants, location, is_streaming, provides_stream, event_name))
        #addGame = ("INSERT INTO Hosts (Event_id, Game_name) VALUES ('{}', '{}')".format(event_id, game))
        #Insert new Player into the Database
        cursor.execute(addEvent)
        #cursor.execute(addGame)
        conn.commit()
        cursor.close()
        conn.close()

def editEvent():
    pass


def deleteEvent(event):
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

        deletion = ("DELETE FROM Event WHERE Event_id = '{}' CASCADE".format(event) )


def userInEvent(eventId, username):
    try:
        conn = mysql.connector.connect(user=MY_SQL_CONNECTION[0],
        password=MY_SQL_CONNECTION[1], host=MY_SQL_CONNECTION[2],
        database=MY_SQL_CONNECTION[3], buffered=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong w/ username and password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Test database doesn\'t exist')
        else:
            print(err)
    else:
        # Check to see that they're registered for the event
        cursor = conn.cursor()
        eventId = int(eventId)
        cursor.execute("SELECT * FROM Competes_in WHERE Username='{}' and Event_id='{}'".format(username, eventId))
        results = []
        for r in cursor:
            results.append(r)
        if len(results) == 1:
            return True
        else:
            return False
        cursor.close()
        conn.close()


def registerForEvent(eventId, username):
    try:
        conn = mysql.connector.connect(user=MY_SQL_CONNECTION[0],
        password=MY_SQL_CONNECTION[1], host=MY_SQL_CONNECTION[2],
        database=MY_SQL_CONNECTION[3], buffered=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong w/ username and password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Test database doesn\'t exist')
        else:
            print(err)
    else:
        # Check to make sure that the eventId and username are in the database.
        usernameCursor = conn.cursor()
        eventCursor = conn.cursor()
        cursor = conn.cursor()
        eventId = int(eventId)
        usernameCursor.execute("SELECT * FROM Player WHERE Username='{}'".format(username))
        eventCursor.execute("SELECT * FROM Event WHERE Event_id='{}'".format(eventId))
        usernameResults = []
        eventResults = []
        for r in usernameCursor:
            usernameResults.append(r)
        usernameCursor.close()
        for r in eventCursor:
            eventResults.append(r)
        eventCursor.close()
        # Found them!
        if len(usernameResults) == 1 and len(eventResults) == 1:
            # Add the username and eventId to the Competes_in table.
            cursor.execute("INSERT INTO Competes_in (Event_id, Username) VALUES ('{}', '{}')".format(eventId, username))
            conn.commit()
        cursor.close()
        conn.close()


def unregisterFromEvent(eventId, username):
    try:
        conn = mysql.connector.connect(user=MY_SQL_CONNECTION[0],
        password=MY_SQL_CONNECTION[1], host=MY_SQL_CONNECTION[2],
        database=MY_SQL_CONNECTION[3], buffered=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong w/ username and password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Test database doesn\'t exist')
        else:
            print(err)
    else:
        # Check to see that they're registered for the event
        cursor = conn.cursor()
        eventId = int(eventId)
        cursor.execute("SELECT * FROM Competes_in WHERE Username='{}' and Event_id='{}'".format(username, eventId))
        results = []
        for r in cursor:
            print(r)
            results.append(r)
        if len(results) == 1:
            deleteCursor = conn.cursor()
            deleteCursor.execute("DELETE FROM Competes_in WHERE Username='{}' and Event_id='{}'".format(username, eventId))
            deleteCursor.close
        else:
            return
        conn.commit()
        cursor.close()
        conn.close()


def deleteEvent(eventId):
    pass
