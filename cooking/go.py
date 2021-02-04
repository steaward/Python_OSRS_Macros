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

def getCookCoords():
    print("Getting theiving coords ")
    with open('cook.json', 'r') as file:
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

def cook():
    coords = getCookCoords()["coordinates"]
    offset = random.randint(0,5)
    for i in range(len(coords)):       
        moveToCoord(coords[i][0] + offset,coords[i][1]+ offset, random.uniform(0.1, 0.3), 0, coords[i][4], False)
        if i == 0:
            time.sleep(3) 
        if i == 1:
            time.sleep(70)
            

def bank():
    print("Banking..")
    coords = getBankCoords()["coordinates"]
    for i in range(len(coords)):
        if i == 0:
            time.sleep(3)
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4], False, True)
       
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
        if now < timeToRun:
            # every 15 minutes, take a break (33% of the time)
            if now.minute % 15 == 0:
                factor = random.randrange(1,15)
                if factor == 3:
                    print("Taking a break...")
                    time.sleep(random.randrange(60,120))

            print("Running at current time: " + str(datetime.now()) + " Time to end: " + str(timeToRun))
            moveType = random.choice(movementType)


            cook()
            bank()
