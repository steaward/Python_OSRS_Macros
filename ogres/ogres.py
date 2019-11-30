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
timesToReload = [30, 31, 32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
timesToHitOgres = [0.7,0.8,0.9, 1,1.5, 1.6]

# Functions
def click(t, mouse_button):
    time.sleep(t)
    pyautogui.click(button=mouse_button)

def loadCannon(x,y,t,mtype):
    print("Loading cannon x: " + str(x) + ", y: " + str(y))
    pyautogui.moveTo(x,y,t,mtype)
    click(t, 'left')
   

def hitOgre(x,y,t,mtype):
    print("Hitting ogre x: " + str(x) + ", y: " + str(y))
    pyautogui.moveTo(x,y,t,mtype)
    click(t, 'left')

def getCannonCoords():
    print("Getting cannon coords...")
    with open('cannon.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def getOgreCoords():
    print("Getting ogre coords...")
    with open('ogres.json', 'r') as file:
                loaded_data = json.load(file)   
    return loaded_data

def logout():
    print("Logging out...")
    with open('logout.json', 'r') as file:
                loaded_data = json.load(file)
            
    coords = loaded_data["coordinates"]
    pyautogui.moveTo(coords[0][0], coords[0][1], 1)
    click(1, 'right')
    pyautogui.moveTo(coords[1][0], coords[1][1], 1)
    click(1, 'left')
    pyautogui.moveTo(coords[2][0], coords[2][1], 1)
    click(1, 'left')
    pyautogui.moveTo(coords[3][0], coords[3][1], 1)
    click(1, 'left')


# Main
if __name__ == '__main__':
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting to kill ogres")
    cannonCoords = getCannonCoords()["coordinates"]
    ogreCoords = getOgreCoords()["coordinates"]

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

            #load cannon
            cannonCoord = random.choice(cannonCoords)
            loadCannon(cannonCoord[0], cannonCoord[1], 1, moveType)
            time.sleep(2)
            
            # wait to reload
            reloadTime = random.choice(timesToReload)

            t_end = time.time() + reloadTime
            while time.time() < t_end:
                 # hit ogre
                ogreCoord = random.choice(ogreCoords)
                timeToHit = random.choice(timesToHitOgres)
                hitOgre(ogreCoord[0], ogreCoord[1], timeToHit, moveType)
                time.sleep(0.5)
            
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)

