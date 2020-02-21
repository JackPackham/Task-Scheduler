import json

def readJson(file):
    with open(file) as readJs:
        currentTask = json.load(readJs)
    return currentTask




def writeJson(dicts,file):
    with open(file,"w") as writeJs:
        json.dump(dicts,writeJs)




def Write(tasks,FILE):

    WRITING = True

    while(WRITING):

        taskName = input("enter task name: ")
        taskDate = input("enter task date in YYYY-MM-DD format: ")
        tasks[taskName] = taskDate

        goAgain = input("go again, YES or NO: ").lower()
        if goAgain == "yes":
            WRITING = True
        elif goAgain == "no":
            WRITING = False
        else:
            print("incorrect input, choose YES or NO: ")

    currentTask = tasks
    writeJson(currentTask,FILE)