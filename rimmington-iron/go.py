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

def getCoords(type):
    if type == "mine":
        # variation = random.randint(1,1)
        print("Getting mining coords...")
        coordFile = 'mine.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "bank":
        print("Getting banking coords...")
        coordFile = 'bank.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data
    
    if type == "return":
        print("Getting banking coords...")
        coordFile = 'return.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

def click(t):
    pyautogui.click(button='left')
    time.sleep(t)

def moveToCoord(x, y, time, step):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + " wait time: " +str(time) + " delay: " + str(delay))
    pyautogui.moveTo(x,y)
    # doubleClick = random.randint(0,3)
    # if doubleClick == 2:
    #     click(0.5)

    click(time + delay)

def returnToMine():
    print("Returning to mine...")
    coords = getCoords("return")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)    

    return True

def mine(i):
    print("Starting to mine: " + str(i) + "/14 tasks completed.")
    coords = getCoords("mine")["coordinates"]
    offset = random.randint(0,2)
    timeOffSet = random.randrange(100,999)/1000
    for i in range(len(coords)):
        moveToCoord(coords[i][0] + offset,coords[i][1] + offset, coords[i][2] + timeOffSet, i)

    time.sleep(6)

def bank():
    print("Returning to bank...")
    coords = getCoords("bank")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
    
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

    atBank = False
    while True:
        print("Beginning trip #" + str(tripNumber))

        if startAtBank == 1:
            atMine = returnToMine()
            startAtBank = 0
        else:
            atMine = True
        
        if atBank:
            atMine = returnToMine()
            atBank = False

        if not atBank and atMine:
            i = 0
            while i < 15:
                mine(i)
                i = i + 1

            atBank = bank()

        tripNumber = tripNumber + 1



