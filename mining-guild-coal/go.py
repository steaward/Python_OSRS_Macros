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

def click(t, btn, doubleClick = False):
    if doubleClick:
        pyautogui.click(button=btn)
        time.sleep(0.25)
    pyautogui.click(button=btn)

    time.sleep(t)

def moveToCoord(x, y, time, btn, step, doubleClick = False):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + " wait time: " +str(time) + " delay: " + str(delay))
    pyautogui.moveTo(x,y)
    # doubleClick = random.randint(0,3)
    # if doubleClick == 2:
    #     click(0.5)

    click(time + delay, btn, doubleClick)

def returnToMine():
    print("Returning to mine...")
    coords = getCoords("return")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3],i)    

    return True

def mine(i):
    print("Starting to mine: " + str(i) + "/" + str(tasks) + " completed.")
    coords = getCoords("mine")["coordinates"]
    offset = random.randint(0,0)
    timeOffSet = random.randrange(100,999)/1000
    for i in range(len(coords)):
        moveToCoord(coords[i][0] + offset,coords[i][1] + offset, coords[i][2] + timeOffSet, coords[i][3], i, True)

    time.sleep(1)

def bank():
    print("Returning to bank...")
    coords = getCoords("bank")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2],coords[i][3], i)
    
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
            atMine = returnToMine()
            startAtBank = 0
        else:
            atMine = True
        
        if atBank:
            atMine = returnToMine()
            atBank = False

        if not atBank and atMine:
            i = 0
            while i < tasks:
                mine(i)
                i = i + 1

            time.sleep(1)
            atBank = bank()

        tripNumber = tripNumber + 1



