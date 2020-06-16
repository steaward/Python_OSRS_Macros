# # # # # # # # # # # # # # # # # # # # # # # #
#   This is a script for RuneScape            #
#                                             #
#   You need 52 agility to use it             #
#                                             #
#                                             #
#                                             #
#   Type: py wildyagil.py n                   #
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
    print("Getting agility coords...")
    with open('coords.json', 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def click(t):
    time.sleep(t)
    pyautogui.click(button='left')
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting cammy agility course...")
    lapped = False
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
            if (not lapped):
                print("1st obstacle.")
                pyautogui.moveTo(coords[0][0], coords[0][1], 0.5)
                click(0)

            
            time.sleep(5)
            print("2nd obstacle.")
            pyautogui.moveTo(coords[1][0], coords[1][1], 0.5)
            click(0)

            
            time.sleep(8)
            print("3rd obstacle.")
            pyautogui.moveTo(coords[2][0], coords[2][1], 0.5)
            click(0)

            
            time.sleep(7)
            print("4th obstacle.")
            pyautogui.moveTo(coords[3][0], coords[3][1], 0.5)
            click(0)

            
            time.sleep(8)
            print("5th obstacle.")
            pyautogui.moveTo(coords[4][0], coords[4][1], 0.5)
            click(0)

            
            time.sleep(5)
            print("6th obstacle.")
            pyautogui.moveTo(coords[5][0], coords[5][1], 0.5)
            click(0)

            time.sleep(5)
            print("7th obstacle.")
            pyautogui.moveTo(coords[6][0], coords[6][1], 0.5)
            click(0)

            time.sleep(5)
            print("8th obstacle.")
            pyautogui.moveTo(coords[7][0], coords[7][1], 0.5)
            click(0)

            time.sleep(6)
            print("9th obstacle.")
            pyautogui.moveTo(coords[8][0], coords[8][1], 0.5)
            click(0)

            time.sleep(5)
            print("10th obstacle.")
            pyautogui.moveTo(coords[9][0], coords[9][1], 0.5)
            click(0)

            time.sleep(9)
            print("Endth obstacle.")
            pyautogui.moveTo(coords[9][0], coords[9][1], 0.5)
            click(0)

            lapped = True
            
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)