import json

def readJson(file):
    with open(file,"r") as readJs:
        currentTask = json.load(readJs)
    return currentTask




def writeJson(dicts,file):
    with open(file,"w") as writeJs:
        json.dump(dicts,writeJs)




def wipeJson(file):
    currentTask = dict({})
    writeJson(currentTask,file) 



def jsonToArray(json):
    dateArray = []
    keysArray = []
    for key, value in json.items():
        dateArray.append(value)
        keysArray.append(key)

    return dateArray
    




def sortDates(dateArray):
    
    tempDates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in dateArray]
    tempDates.sort()
    tempSortDates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in tempDates]

    return tempSortDates
   


