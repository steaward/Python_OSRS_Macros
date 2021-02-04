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

def getCoords():
    with open('interact.json', 'r') as file:
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
 

def interact():
    print("Interacted")
    coords = getCoords()["coordinates"]
    moveToCoord(coords[0][0],coords[0][1], coords[0][2], coords[0][3], coords[0][4])
    time.sleep(0.5)

def refresh():
    interactMinute = random.randint(1,15)
    print("Interacting in.... " + str(interactMinute * 60) +" seconds")
    return interactMinute * 60

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
    interactMinute = random.randint(1,1)
    interactSeconds = interactMinute * 60
    print("Interacting in.... " + str(interactSeconds) +" seconds")
    startTime = time.time()
    interacted = False  
    while True:
        now = datetime.now()
        if now < timeToRun:
            # every 15 minutes, take a break (33% of the time)
            if now.minute % 15 == 0:
                factor = random.randrange(1,15)
                if factor == 3:
                    print("Taking a break...")
                    time.sleep(random.randrange(60,120))

            moveType = random.choice(movementType)

            # start at inv space 4:
            runTime = int(time.time() - startTime)  
            # every random minutes eat:
            if (datetime.now().minute % 3 == 0 and not interacted):
                print("Interacting...")
                interact()
                interacted = True
            elif datetime.now().minute % 3 is not 0:
                interacted = False
               

