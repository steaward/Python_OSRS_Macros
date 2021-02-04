# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  #
#     #
#       #
#                                                           #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pyautogui
import pynput
import random
import json
import time
import sys
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller
from pynput.keyboard import Key, Controller as kbController
 
# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
timesToAlch = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
timeToTele = [0.3, 0.4,0.5,0.6,0.7,0.8,0.9, 1]
offset = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

def click(t, btn, useShift = False, doNotDoubleClick = False):
    keyboard = kbController()
    time.sleep(t)
    if (useShift):
        keyboard.press(Key.shift)
        time.sleep(0.1)
        pyautogui.click(button=btn)
        time.sleep(0.3)
        keyboard.release(Key.shift)
    else:
        doubleClick = random.randint(0,3)
        pyautogui.click(button=btn)
        if (doubleClick % 3 == 0 and not doNotDoubleClick):
            print("Double clicking!")
            pyautogui.click(button=btn)


def moveToCoord(x, y, time, step, btn, printCoord = True, doNotDoubleClick = False):
    moveType = random.choice(movementType)
    if (printCoord):
        print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y,time, moveType)

    click(time, btn, False, doNotDoubleClick)

def getBankCoords():
    print("Getting bank coords...")
    with open('bank.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getTheiveCoords():
    print("Getting theiving coords ")
    with open('theive.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getInvCoords():
    print("Getting eat coords...")
    with open('inventory.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def logout():
    print("Logging out...")
    with open('logout.json', 'r') as file:
                loaded_data = json.load(file)

    coords = loaded_data["coordinates"]
    pyautogui.moveTo(coords[0][0], coords[0][1], 1)
    click(1)
    pyautogui.moveTo(coords[1][0], coords[1][1], 1)
    click(1)


def theive(theiveCount, coords):
    print("Thieve count: " + str(theiveCount))
    theiveCount = theiveCount + 1
    offset = random.randint(0,5)
    for i in range(len(coords)):
        moveToCoord(coords[i][0] + offset,coords[i][1]+ offset, random.uniform(0.1, 0.3), 0, coords[i][4], False) 
    if (theiveCount % 28 == 0):
        getCoins()  

    return theiveCount   

def bank():
    print("Banking..")
    coords = getBankCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4], False, True)
        time.sleep(0.5)

def eat(index, coords):
    print("eat at inv space " + str(index))
    moveToCoord(coords[index][0],coords[index][1], coords[index][2], coords[index][3], coords[index][4])

def equipNeck(index, coords):
    print("equipping necklace at inv space " + str(index))
    moveToCoord(coords[index][0],coords[index][1], coords[index][2], coords[index][3], coords[index][4])

def getCoins():
    print("getting coins")
    coords = getInvCoords()["coordinates"]
    moveToCoord(coords[0][0],coords[0][1], coords[0][2], coords[0][3], coords[0][4])


# Main
if __name__ == '__main__':
    
    currentEatIndex = 4

    if len(sys.argv) == 2:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    elif len(sys.argv) == 3:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]))
        currentEatIndex = int(sys.argv[2])
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting to theive")
    while True:
        now = datetime.now()
        invCoords = getInvCoords()["coordinates"]
        if now < timeToRun:
            # every 15 minutes, take a break (33% of the time)
            if now.minute % 15 == 0:
                factor = random.randrange(1,15)
                if factor == 3:
                    print("Taking a break...")
                    time.sleep(random.randrange(60,120))

            print("Running at current time: " + str(datetime.now()) + " Time to end: " + str(timeToRun))
            moveType = random.choice(movementType)

            # start at inv space 4:
            
            currentDodgyNekIndex = 2
            fed = False
            getNecklace = True
            interacted = False
            startTime = time.time()
            theiveCount = 0
            theiveCoords = getTheiveCoords()["coordinates"]
            while(currentEatIndex < 28):               
                theiveCount = theive(theiveCount, theiveCoords)
                time.sleep(random.uniform(0.1, 0.3))
                runTime = int(time.time() - startTime)  
                print("Run time in seconds: " + str(runTime))    
                # every 1 minutes eat:
                if (runTime is not 0 and runTime % 60 == 0 and not fed):
                    eat(currentEatIndex, invCoords)
                    currentEatIndex = currentEatIndex + 1
                    fed = True
                elif (runTime % 60 is not 0):
                    fed = False

                #every 3 minutes, sleep for 5 seconds so we can ues mouse for splasher to interact:
                if (datetime.now().minute % 3 == 0 and not interacted):
                    time.sleep(15)
                    interacted = True
                elif(datetime.now().minute %3 is not 0):
                    interacted = False

                # every 4 minutes change necklaces
                if(runTime is not 0 and runTime %  240 == 0 and getNecklace):
                    equipNeck(currentDodgyNekIndex, invCoords)
                    currentDodgyNekIndex = currentDodgyNekIndex + 1
                    getNecklace = False
                elif(runTime  % 240 is not 0):
                    getNecklace = True

            currentEatIndex = 4
            currentDodgyNekIndex = 2
            bank()

