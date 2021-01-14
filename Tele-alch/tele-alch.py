# # # # # # # # # # # # # # # # # # # # # # # #
#   This is a script for RuneScape            #
#                                             #
#   You need 55 magic to use it               #
#                                             #
#   Please start with your magic window open. #
#                                             #
#   Type: py tele-alch n                      #
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
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
timesToAlch = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
timeToTele = [0.3, 0.4,0.5,0.6,0.7,0.8]
# Functions
def click(t):
    time.sleep(t)
    pyautogui.click(button='left')

def alch(x,y,t,mtype):
    print("Alching x: " + str(x) + ", y: " + str(y))
    pyautogui.moveTo(x,y,t,mtype)
    click(t)
    click(1.5)

def tele(x,y,t,mtype):
    print("Teleing x: " + str(x) + ", y: " + str(y))
    pyautogui.moveTo(x,y,t,mtype)
    click(t)

def getAlchCoords():
    print("Getting alch coords...")
    with open('alch_coords.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getTeleCoords():
    print("Getting alch coords...")
    with open('tele_coords.json', 'r') as file:
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

# Main
if __name__ == '__main__':
    alchOnly = True
    teleOnly = False
    if len(sys.argv) == 2:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    elif len(sys.argv) == 3:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
        alchOnly = True
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting tele alch")
    alchCoords = getAlchCoords()["coordinates"]
    teleCoords = getTeleCoords()["coordinates"]
    
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

            # TELE
            if not alchOnly:
                timeToClickTele = random.choice(timeToTele) 
                goToTeleCoords = random.choice(teleCoords)
                tele(goToTeleCoords[0], goToTeleCoords[1], timeToClickTele, moveType)

            # ALCH
            if not teleOnly:
                timeToClickAlch = random.choice(timesToAlch) 
                goToAlchCoords = random.choice(alchCoords)
                alch(goToAlchCoords[0], goToAlchCoords[1],timeToClickAlch,moveType)
                time.sleep(random.randint(0,3))
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)

        

    
       

