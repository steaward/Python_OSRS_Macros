# # # # # # # # # # # # # # # # # # # # # # # #
#   This is a script for RuneScape            #
#                                             #
#   You need 40 agility to use it             #
#                                             #
#                                             #
#                                             #
#   Type: py go.py n running marks            #
#   where n = time(hours) to run for.         #
#   optional: running = 1 or 0                #
#             marks = 1 or 0                  #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #


import pyautogui
import pynput
import random
import json
import time
import sys
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
running = False
laps = 0

def getCoords():
    variation = random.randint(1,1)
    print("Getting agility coords...")
    coordFile = 'coords.json'
    with open(coordFile, 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getMarkCoords():
    variation = random.randint(1,1)
    print("Getting agility coords...")
    coordFile = 'marks.json'
    with open(coordFile, 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def click(t):
    pyautogui.click(button='left')

    if running:
        t = t - 0.5

    time.sleep(t)

def moveToCoord(x, y, time, step):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y))
    pyautogui.moveTo(x,y)
    click(time)



if __name__ == '__main__':
    if len(sys.argv) > 1:

        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
        try:
            if sys.argv[2] != None:
                running = True
            
            if sys.argv[3] != None:
                laps = 5
        except:
            print("Not all arguments given.")

    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting canifis agility course...")
    
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

            # MOVE
            if laps % 5 == 0 and laps != 0:
                print("Getting marks, lap # " + str(laps))
                coords = getMarkCoords()["coordinates"]
                for i in range(len(coords)):
                    moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
                laps = laps + 1

            else:
                print("No marks this run, lap # " + str(laps))
                coords = getCoords()["coordinates"]
                for i in range(len(coords)):
                    moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
                laps = laps + 1
            
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)