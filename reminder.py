import datetime
from datetime import date
import time

def jsonToArray(json):
    dateArray = []
    keysArray = []
    for key, value in json.items():
        dateArray.append(value)
        keysArray.append(key)

    return dateArray
    




def sortDates(dateArray):
    try:
        tempDates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in dateArray]
        tempDates.sort()
        tempSortDates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in tempDates]
        print(tempSortDates)

        return tempSortDates
    except:
        print("Something went wrong with the .json file")




def reminderMain(dateArray,isRunning):

    
    tempDate = date.today()
    CurrentDate = tempDate.strftime("%Y-%m-%d")

    while(isRunning):
        time.sleep(1)
        dateEntry = sortDates(jsonToArray(dateArray))
        if dateEntry[0] == CurrentDate:
            print("do shit!")
        elif (buttonpress)

        


        
