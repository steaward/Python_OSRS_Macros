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
        # if (doubleClick % 3 == 0 and not doNotDoubleClick):
        #     print("Double clicking!")
        #     pyautogui.click(button=btn)


def moveToCoord(x, y, time, step, btn, printCoord = True, doNotDoubleClick = False):
    moveType = random.choice(movementType)
    if (printCoord):
        print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y,time, moveType)

    click(time, btn, False, doNotDoubleClick)

def getPickupCoords():
    print("Getting pickup coords ")
    with open('pickup.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getBankCoords():
    print("Getting bank coords...")
    with open('bank.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getCastSpellCoords():
    print("Getting cast coords...")
    with open('spell.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getWithdrawCoords():
    print("Getting withdraw coords...")
    with open('withdraw.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def bank(closeBank):
    coords = getBankCoords()["coordinates"]
    # offset = random.randint(0,5)
    offset = 0 
    for i in range(len(coords)):
        if (i == 3 and not closeBank):
            return
        else:         
            moveToCoord(coords[i][0] + offset,coords[i][1]+ offset, random.uniform(0.1, 0.3), 0, coords[i][4], False) 
            time.sleep(1)
        
def withdraw():
    print("withdrawing items..")
    coords = getWithdrawCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4], False, True)

def castSpell():
    print("Casting spell...")
    coords = getCastSpellCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4], False, True)

def pickup():
    print("Picking up items")
    coords = getPickupCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4], False, True)
# Main
if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    elif len(sys.argv) == 3:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]))

    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting to make glass")
    startTime = time.time()
    pickingUpGlass = False
    while True:
        now = datetime.now()   
        runTime = int(time.time() - startTime) 
        if now < timeToRun:
            # every 15 minutes, take a break (33% of the time)
            if now.minute % 15 == 0:
                factor = random.randrange(1,15)
                if factor == 3:
                    print("Taking a break...")
                    time.sleep(random.randrange(60,120))

            print("Running at current time: " + str(datetime.now()) + " Time to end: " + str(timeToRun))
            moveType = random.choice(movementType)

            # every 1.5 minutes pickup fallen glass
            print("Current runtime: " + str(runTime))
            if (runTime is not 0 and runTime > 90 and not pickingUpGlass):
                bank(True)
                pickup()
                bank(False)
                withdraw()
                castSpell()
                pickingUpGlass = True
                startTime = time.time()
            else:
                pickingUpGlass = False

            if (not pickingUpGlass):
                bank(False)
                withdraw()
                castSpell()

