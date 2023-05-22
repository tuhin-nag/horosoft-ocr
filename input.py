import datetime

#TODO validation for start/end year

def getdtinput(): #start and end date for program
    try:
        start = input('Enter start date(14,05,2021): ')
        day, month, year = map(int, start.split(','))
    except:
        print('enter input in given format')
        
    try:
        starttime = input('Enter start time (05:30): ')
        hour, minute = map(int, starttime.split(':'))
    except:
        print('enter input in given format')
        

    startdate = datetime.datetime(year, month, day, hour, minute)

    try:
        end = input('Enter end date(14,05,2021): ')
        day, month, year = map(int, end.split(','))
    except:
        print('enter input in given format')
        

    enddate = datetime.datetime(year, month, day, hour, minute)

    return startdate, enddate

def getinterval(): #interval in minutes
    
    minutes = int(input('interval in minutes: '))
    interval = datetime.timedelta(minutes = minutes)
    return interval

def hoursperday(): #hours per day before moving on to next day
    hours = int(input('hours per day: '))
    hpd = datetime.timedelta(hours = hours)
    return hpd