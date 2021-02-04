# # # # # # # # # # # # # # # # # # # # # # # #
#   This is a script for RuneScape            #
#                                             #
#   You need 30 mining to use it              #
#                                             #
#                                             #
#                                             #
#   Type: py go.py n                          #
#   where n = time(hours) to run for.         #
#   Time to 99 mining = 150 hours.            #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #


import pyautogui
import pynput
import random
import json
import time
import sys
import cv2
import numpy as np
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
delay = 0
tasks = 21
atBank = False

def getCoords(type):
    if type == "bank":
        # variation = random.randint(1,1)
        print("Getting banking coords...")
        coordFile = 'bank.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "furnace":
        print("Getting furnance coords...")
        coordFile = 'furnace.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "deposit":
        print("Getting deposit coords...")
        coordFile = 'deposit.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data
    

def click(t, btn, doubleClick = False):
    if doubleClick:
        pyautogui.click(button=btn)
        time.sleep(0.25)
    pyautogui.click(button=btn)

    time.sleep(t)

def moveToCoord(x, y, tm, btn, step, doubleClick):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + " wait time: " +str(tm) + " delay: " + str(delay))
    moveType = random.choice(movementType)
    moveSpeed = random.uniform(0.1, 1.5)
    pyautogui.moveTo(x,y, moveSpeed, moveType)
    if doubleClick == True:
        click(0.25, btn)

    click(tm + delay, btn)


def smelt():
    print("Starting to smelt cannon balls... ")
    coords = getCoords("furnace")["coordinates"]
    offset = random.randint(0,0)
    timeOffSet = random.randrange(100,999)/1000
    for i in range(len(coords)):
        moveToCoord(coords[i][0] + offset, coords[i][1] + offset, coords[i][2] + timeOffSet, coords[i][3], i, True)

    time.sleep(1)

def deposit():
    print("Depositing... ")
    atBank = True
    coords = getCoords("deposit")["coordinates"]
    offset = random.randint(0,0)
    timeOffSet = random.randrange(100,999)/1000
    for i in range(len(coords)):
        moveToCoord(coords[i][0] + offset, coords[i][1] + offset, coords[i][2] + timeOffSet, coords[i][3], i, True)

    time.sleep(1)
def bank():
    print("Returning to bank...")
    coords = getCoords("bank")["coordinates"]
    if atBank:
        startingCoord = 1
    else:
        startingCood = 0
    for i in range(startingCood,len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2],coords[i][3], i, False)
    
    return True


if __name__ == '__main__':
    startAtBank = 0
    delay = 0
    tripNumber = 1
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )

        if len(sys.argv) > 2:
            startAtBank = int(sys.argv[2])
        
        if len(sys.argv) > 3:
            delay = int(sys.argv[3])

        if len(sys.argv) > 4:
            tasks = int(sys.argv[4])

    atBank = False
    print("Starting up.... # of tasks to complete per trip: " + str(tasks))
    while True:
        print("Beginning trip #" + str(tripNumber))

        if startAtBank == 1:
            deposit()
            smelt()
        
        bank()
        time.sleep(1)
        smelt()
        time.sleep(170)
        deposit()
        time.sleep(1)

        



