import datetime

def jsonToArray(json):
    dateArray = []
    keysArray = []
    for key, value in json.items():
        dateArray.append(value)
        keysArray.append(key)

    return dateArray
    return keysArray
    




def sortDates(dateArray):
    tempDates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in dateArray]
    tempDates.sort()
    tempSortDates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in tempDates]
    print(tempSortDates)
    






def search():
    with open("tasks.json") as tasks:
        print ("hello")




def convertDate(date):
    year,month,day = date.split("-")



def reminderMain(dict):
    sortDates(jsonToArray(dict))
