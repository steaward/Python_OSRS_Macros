# # # # # # # # # # # # # # # # # # # # # # # #
#   This is a script for RuneScape            #
#                                             #
#   It will cast super heat to make steel     #
#                                    bars     #
#                                             #
#                                             #
#   Type: py go.py n                   #
#   where n = time(hours) to run for.         #
#   Time to 99 mage = 150 hours.              #
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
from pynput.keyboard import Key, Controller as kbController

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
dropping = False

def getCoords(type):
    if type == "drop":
        print("Getting drop coords...")
        coordFile = 'drop.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "fill":
        print("Getting fill water coords...")
        coordFile = 'fill.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "heat":
        print("Getting heating coords...")
        coordFile = 'heat.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "make":
        print("Getting make coords...")
        coordFile = 'make.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "mine":
        print("Getting mine coords...")
        coordFile = 'mine.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data
    
    if type == "soft":
        print("Getting soft coords...")
        coordFile = 'soft.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

def click(t, btn):
    pyautogui.click(button=btn)
    time.sleep(t)

def moveToCoord(x, y, tm, step, btn, dropping = False):
    keyboard = kbController()
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(tm))
    pyautogui.moveTo(x,y)

    if (dropping):
        time.sleep(0.5)
        print("pressing shift:")
        keyboard.press(Key.shift)
        time.sleep(0.1)
        pyautogui.click(button='left')
        pyautogui.click(button='left')
        keyboard.release(Key.shift)

    else:
        click(tm + delay, btn)

    # if (dropping):
    #     keyboard.release('shift')

    

def fill():
    print("Filling water...")
    coords = getCoords("fill")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])  

        if i == len(coords):
            print("Finished filling water.")      

def drop():
    print("Droping items...")

    coords = getCoords("drop")["coordinates"]
    
    moveToCoord(coords[0][0],coords[0][1], coords[0][2], coords[0][3], coords[0][4], True)

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4], True)
    

        
def mine():
    print("Mining ore...")
    coords = getCoords("mine")["coordinates"]
    # move to spot
    moveToCoord(coords[0][0],coords[0][1], coords[0][2], coords[0][3], coords[0][4])
    time.sleep(2)
    # mine both ores 7 times (14 total)
    for i in range(7):
        moveToCoord(coords[1][0],coords[1][1], coords[1][2], coords[1][3], coords[1][4])
        time.sleep(1)
        moveToCoord(coords[2][0],coords[2][1], coords[2][2], coords[2][3], coords[2][4])
        time.sleep(1)


def make():
    print("Making pots...")
    coords = getCoords("make")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])

def heat():
    print("Heating pots...")
    coords = getCoords("heat")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])

def softClay():
    print("Making soft clay...")
    coords = getCoords("soft")["coordinates"]

    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])




if __name__ == '__main__':
    startingCoord = 0
    delay = 0
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )

        if len(sys.argv) > 2:
            startingCoord = int(sys.argv[2])
        
        if len(sys.argv) > 3:
            delay = int(sys.argv[3])

        

    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting to super heat steel bars...")
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

          
            mine()
            time.sleep(1)
            softClay()     
            time.sleep(15)
            fill()
            time.sleep(10)
            make()
            time.sleep(25)
            heat()
            time.sleep(65)
            drop()
            time.sleep(10)
      
                
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)