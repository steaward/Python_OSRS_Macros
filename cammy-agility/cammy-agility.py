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

def getCoords(getmarks):
    loaded_data = []
    if (getmarks is False):
        print("Getting agility coords without marks...")
        with open('no-marks-coords.json', 'r') as file:
                    loaded_data = json.load(file)
    else:
        print("Getting agility coords with marks...")
        with open('coords.json', 'r') as file:
                loaded_data = json.load(file)

    return loaded_data

def click(t):
    time.sleep(t)
    pyautogui.click(button='left')
    
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
        checkForMarksArg = 0
    elif (len(sys.argv) == 3):
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
        checkForMarksArg = int(sys.argv[2])
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

    print("Starting cammy agility course...")
    lapped = False
    checkForMarks = False
    numberOfLaps = 0
    while True:
        if (checkForMarksArg == 1):
            checkForMarks = True
        elif (numberOfLaps % 5 == 0 and numberOfLaps is not 0):
            checkForMarks = True
        else:
            checkForMarks = False

        checkForMarksArg = 0 # revert this back now that we are going to be looping over and over and want to hit the second check.
        now = datetime.now()
        if now < timeToRun:
            # every 15 minutes, take a break (33% of the time)
            if now.minute % 15 == 0:
                factor = random.randrange(1,15)
                if factor == 3:
                    print("Taking a break...")
                    time.sleep(random.randrange(60,120))

            print("Running at current time: " + str(datetime.now()) + " Time to end: " + str(timeToRun))
            print("Run #" + str(numberOfLaps))

            moveType = random.choice(movementType)

            if (not checkForMarks):
                coords = getCoords(False)["coordinates"]
            else:
                coords = getCoords(True)["coordinates"]


            # MOVE
            if (checkForMarks is True):
                print("Looking for marks this run.")
                numberOfLaps = numberOfLaps + 1
                if (not lapped):
                    print("1st obstacle.")
                    pyautogui.moveTo(coords[0][0], coords[0][1], 0.5)
                    click(0)

                if (not lapped):
                    time.sleep(5)
                else:
                    time.sleep(10)

                
                print("Mark Of Grace #1")
                pyautogui.moveTo(coords[1][0], coords[1][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)
           
                time.sleep(3)
                print("2nd obstacle.")
                pyautogui.moveTo(coords[2][0], coords[2][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)
                
                time.sleep(6)
                print("Mark Of Grace #2")
                pyautogui.moveTo(coords[3][0], coords[3][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)
            
                time.sleep(3)
                print("Mark Of Grace #3")
                pyautogui.moveTo(coords[4][0], coords[4][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)
                
                time.sleep(5)
                print("3rd obstacle.")
                pyautogui.moveTo(coords[5][0], coords[5][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(9)
                print("Mark Of Grace #4")
                pyautogui.moveTo(coords[6][0], coords[6][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(4)
                print("5th obstacle.")
                pyautogui.moveTo(coords[7][0], coords[7][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(7)
                print("6th obstacle.")
                pyautogui.moveTo(coords[8][0], coords[8][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)


                time.sleep(6)
                print("Mark Of Grace #5")
                pyautogui.moveTo(coords[9][0], coords[9][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)


                time.sleep(6)
                print("7th obstacle.")
                pyautogui.moveTo(coords[10][0], coords[10][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(9)
                print("8th obstacle.")
                pyautogui.moveTo(coords[11][0], coords[11][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)


                time.sleep(9)
                print("Endth obstacle.")
                pyautogui.moveTo(coords[12][0], coords[12][1], 0.5, moveType)
                click(0)

                lapped = True
            else:
                print("Skipping marks.")
                numberOfLaps = numberOfLaps + 1

                if (not lapped):
                    print("1st obstacle.")
                    pyautogui.moveTo(coords[0][0], coords[0][1], 0.5, moveType)
                    click(0)

                if (not lapped):
                    time.sleep(5)
                else:
                    time.sleep(10)

                print("2nd obstacle.")
                pyautogui.moveTo(coords[1][0], coords[1][1], 0.5, moveType)
                click(0)
                
                moveType = random.choice(movementType)


                time.sleep(8)
                print("3rd obstacle.")
                pyautogui.moveTo(coords[2][0], coords[2][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(10)
                print("4th obstacle.")
                pyautogui.moveTo(coords[3][0], coords[3][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(6)
                print("5th obstacle.")
                pyautogui.moveTo(coords[4][0], coords[4][1], 0.5, moveType)
                click(0)

                time.sleep(6)
                print("6th obstacle.")
                pyautogui.moveTo(coords[5][0], coords[5][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(5.5)
                print("7th obstacle.")
                pyautogui.moveTo(coords[6][0], coords[6][1], 0.5, moveType)
                click(0)

                moveType = random.choice(movementType)

                time.sleep(9)
                print("8th obstacle.")
                pyautogui.moveTo(coords[7][0], coords[7][1], 0.5, moveType)
                click(0)

                lapped = True
            
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)