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
        curTime = datetime.now()
        # Format used to convert SQL Datetime to Python's datetime
        dateFormat = '%Y-%m-%d %H:%M:%S'
        # The list of dicts that we'll be returning.
        collectedEvents = []
        cursor.exectue("SELECT * FROM Event")

        for r in cursor:
            eventTime = datetime.datetime.strptime(r[1])
            # Only grab events that have not happened yet.
            if eventTime > curTime:
                eventInfo['id'] = r[0]
                eventInfo['event-date'] = r[1]
                eventInfo['prize-money'] = r[2]
                eventInfo['max-players'] = r[3]
                eventInfo['location'] = r[4]
                eventInfo['start-time'] = r[5]
                collectedEvents.append(eventInfo)
        return collectedEvents
