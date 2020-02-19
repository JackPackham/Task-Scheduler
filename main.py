import json
import datetime

RUNNING = True

def checkDates(dicts):
    for key in dicts:
        print(key)


def convertStrings(date):
    year,month,day = date.split("-")



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
        exec("readwrite.py")       
        RUNNING = False   

    else:
        print("incorrect try again")
        
