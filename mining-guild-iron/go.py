
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
        doubleClick = random.randint(0,3)
        pyautogui.click(button='left')
        if (doubleClick % 3 == 0):
            pyautogui.click(button='left')


def moveToCoord(x, y, time, step, btn):
    moveType = random.choice(movementType)
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y,time, moveType)

    click(time)

def getMiningCoords():
    print("Getting mining coords...")
    with open('mine.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data


def getBankCoords():
    print("Getting bank coords...")
    with open('bank.json', 'r') as file:
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

def mine():
    print("Mining..")
    coords = getMiningCoords()["coordinates"]
    moveToCoord(coords[0][0],coords[0][1], coords[0][2], coords[0][3], coords[0][4])
    time.sleep(3)
    i = 0
    while (i < 9):
        time.sleep(1)
        offset = random.randint(0,3)
        moveToCoord(coords[1][0] + offset,coords[1][1] + offset, coords[1][2], coords[1][3], coords[1][4])
        time.sleep(1)
        offset = random.randint(0,3)
        moveToCoord(coords[2][0] + offset,coords[2][1]+ offset, coords[2][2], coords[2][3], coords[2][4])
        time.sleep(1)
        offset = random.randint(0,3)
        moveToCoord(coords[3][0]+ offset,coords[3][1]+ offset, coords[3][2], coords[3][3], coords[3][4])
        i = i+1

    moveToCoord(coords[1][0],coords[1][1], coords[1][2], coords[1][3], coords[1][4])



def bank():
    print("Banking..")
    coords = getBankCoords()["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])
        if (i == 0):
            time.sleep(4)


# Main
if __name__ == '__main__':
    if len(sys.argv) == 2:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    elif len(sys.argv) == 3:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting mine")
 
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

            mine();
            time.sleep(1)
            bank();
