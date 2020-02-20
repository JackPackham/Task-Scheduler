import json

#+=======================================================+
#+=======================================================+

def readJson(file):
    with open(file) as readJs:
        currentTask = json.load(readJs)
        print (currentTask)
    return currentTask




def writeJson(dicts,file):
    with open(file,"w") as writeJs:
        json.dump(dicts,writeJs)









