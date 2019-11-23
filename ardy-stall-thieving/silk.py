
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

def click(t, useShift = False):
    keyboard = kbController()
    time.sleep(t)
    if (useShift):
        keyboard.press(Key.shift)
        time.sleep(0.1)
        pyautogui.click(button='left')
        time.sleep(0.3)
        keyboard.release(Key.shift)
    else:
        pyautogui.click(button='left')


def getStallCoords():
    print("Getting alch coords...")
    with open('stall.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data


def getDropCoords():
    print("Getting alch coords...")
    with open('drop.json', 'r') as file:
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

def thieve(x,y,t,mtype):
    print("Thieving stall at x: " + str(x) + ", y: " + str(y))
    pyautogui.moveTo(x,y,t,mtype)
    click(t)

def drop(x,y,t,mtype):
    print("Dropping silk at x: " + str(x) + ", y: " + str(y))
    pyautogui.moveTo(x,y,t,mtype)
    click(t, True)


# Main
if __name__ == '__main__':
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting tele alch")
    stallCoords = getStallCoords()["coordinates"]
    dropCoords = getDropCoords()["coordinates"]
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

            #  THIEVE
            theiveCoords = random.choice(stallCoords)
            timeToClick = random.choice(offset)
            thieve(theiveCoords[0], theiveCoords[1], timeToClick, moveType)

            # DROP ITEM
            itemdropCoords = random.choice(dropCoords)
            drop(itemdropCoords[0], itemdropCoords[1],timeToClick + 0.4,moveType)

            time.sleep(4)
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)