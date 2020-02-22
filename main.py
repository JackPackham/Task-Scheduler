import json
import time
from readwrite import *
from reminder import *

RUNNING = True
FILE = "tasks.json"
currentTask = readJson(FILE)





while(RUNNING):

    print ("1. write new reminder")
    print ("2. run reminder app")
    print ("3. wipe .json")
    print ("4. exit")

    rorw = input().lower()
    


    if rorw == "4":
        exit()


    elif rorw == "3":
        wipeJson(FILE)


    elif rorw == "2":

        reminderMain(currentTask,RUNNING)


    elif rorw == "1":

        Write(currentTask,FILE)  


    else:
        print("incorrect try again")
        
