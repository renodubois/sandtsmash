from setup import MY_SQL_CONNECTION
import mysql.connector
import datetime

def getCurrentEvents():
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
            eventTime = datetime.datetime.strptime(r[1])
            # Only grab events that have not happened yet.
            if eventTime > curTime:
                eventInfo['id'] = r[0]
                eventInfo['event-date'] = datetime.datetime.strptime(r[1])
                eventInfo['entryfee'] = float(r[2])
                eventInfo['max-players'] = r[3]
                eventInfo['location'] = r[4]
                eventInfo['name'] = r[7]
                collectedEvents.append(eventInfo)
        return collectedEvents


def getFinishedEvents():
    pass

def eventValidation(form):
    #Import all of the form information into variables
    event_id = form['event_id']
    event_date = form['event_date']
    entry_fee = form['entry_fee']
    max_participants = form['max_participants']
    location = form['location']
    is_streaming = form['is_streaming']
    provides_stream = form['provides_stream']
    #Create list to hold all the errors
    error = []
    if event_id = '':
        pass
        error.append('')
    if type(event_date) is datetime
    if event_date == '':
        error.append('Event date field must be filled out!')
    if event_date <= NOW():
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
        event_id = form['event_id']
        event_date = form['event_date']
        entry_fee = form['entry_fee']
        max_participants = form['max_participants']
        location = form['location']
        is_streaming = form['is_streaming']
        provides_stream = form['provides_stream']
        game = form['game']
        
        addEvent = ("INSERT INTO Event "
                   "(Event_id, Event_date, Entry_fee, Max_participants, Location, Is_streaming, Provides_stream)"
                   "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(event_id, event_date, entry_fee, max_participants, location, is_streaming, provides_stream))
        addGame = ("INSERT INTO Hosts "
                  "(Event_id, Game_name)"
                  "VALUES ('{}', '{}')".format(event_id, game))
        #Insert new Player into the Database
        cursor.execute(addEvent)
        cursor.execute(addGame)
        conn.commit()
        cursor.close()
        conn.close()

def editEvent():
    pass

def deleteEvent():
    pass
