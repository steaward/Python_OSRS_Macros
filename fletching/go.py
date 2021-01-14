
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

def moveToCoord(x, y, time, step, btn):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y)

    click(time)


def getCoords():
    print("Getting alch coords...")
    with open('coords.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data


def getFletchingCoords():
    print("Getting alch coords...")
    with open('fletchBows.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data


def getBankCoords():
    print("Getting bank coords...")
    with open('bank.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data



def getBankBowsCoords():
    print("Getting bank coords...")
    with open('bankBows.json', 'r') as file:
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

def fletch():
    print("Fletching..")
    coords = getCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])

def bank():
    print("Banking..")
    coords = getBankCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])

def fletchBows():
    print("Fletching bows...")
    coords = getFletchingCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])

def bankBows():
    print("Banking..")
    coords = getBankBowsCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])

# Main
if __name__ == '__main__':
    fletchwBows = False
    if len(sys.argv) == 2:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    elif len(sys.argv) == 3:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
        fletchwBows = True
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting tele alch")
    fletchCoords = getCoords()["coordinates"]
    bakCoords = getBankCoords()["coordinates"]
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

            if fletchwBows:
                fletchBows()
                time.sleep(20)
                bankBows()
                time.sleep(3)
            else:
                fletch()
                time.sleep(49)
                bank()
                time.sleep(3)
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)