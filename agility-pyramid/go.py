# # # # # # # # # # # # # # # # # # # # # # # #
#   This is a script for RuneScape            #
#                                             #
#   You need 75 agility to use it             #
#                                             #
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
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]

def getCoords():
    # variation = random.randint(1,1)
    variation = 2
    print("Getting agility coords...")
    coordFile = 'laps/coords' + str(variation) + '.json'
    with open(coordFile, 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def click(t):
    pyautogui.click(button='left')
    time.sleep(t)

def moveToCoord(x, y, time, step):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y)
    click(time)
    
if __name__ == '__main__':
    startingCoord = 0
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )

        if len(sys.argv) == 3:
            startingCoord = int(sys.argv[2])

    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting wildy agility course...")

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

            coords = getCoords()["coordinates"]
            # MOVE

            for i in range(startingCoord, len(coords)):
                if i == 0:
                    time.sleep(5)
                    
                if i == 4:
                    time.sleep(1)    

                if coords[i][3] == False:
                    moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)

                else:
                    done = False; 
                    while(not done):
                        second = datetime.now().second
                        if (second > 9):
                            second = second % 10
                       
                        if (second == 0 or second == 1):
                            moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
                            done = True;
                        else:
                            print("Not moving...not time yet." + str(second))
                            time.sleep(0.5)
                
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)