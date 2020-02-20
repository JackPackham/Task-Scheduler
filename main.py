import json
import time
import reminder.py
import readwrite.py

RUNNING = True

while(RUNNING):

    print ("1. write new reminder")
    print ("2. run reminder app")
    print ("3. exit")

    rorw = input().lower()
    



    if rorw == "3":
        exit()






    elif rorw == "2":
        print("reminder not coded yet")






    elif rorw == "1":


        currentTask = dict({})
        FILE = "tasks.json"
        WRITING = True

        while(WRITING):

            taskName = input("enter task name: ")
            taskDate = input("enter task date in YYYY-MM-DD format: ")
            tasks[taskName] = taskDate

            goAgain = input("go again YES or NO").lower()

            if goAgain == "yes":
                WRITING = True

            elif goAgain == "no":
                WRITING = False

            else:
                print("incorrect input, choose YES or NO")


        currentTask = tasks
        writeJson(currentTask,FILE)  






    else:
        print("incorrect try again")
        
