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

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
inBank = False
def getCoords(type):
    if type == "bank":
        print("Getting banking coords...")
        coordFile = 'bank.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        print(loaded_data)
        return loaded_data

    if type == "alch":
        print("Getting alch coords...")
        coordFile = 'alch.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "deposit":
        print("Getting depositing coords...")
        coordFile = 'deposit.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

def click(t, btn):
    pyautogui.click(button=btn)
    time.sleep(t)

def moveToCoord(x, y, time, step, btn):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y)

    click(time + delay, btn)
    

def bank():
    print("Banking...")
    coords = getCoords("bank")["coordinates"]
    startingRange = 0
    if inBank:
        startingRange = 1
    
    for i in range(startingRange, len(coords)):
        step = coords[i][3]
        print("Banking, currently at step: " + str(step))
        if step == 6:
            # get 17 pieces of iron
            print("getting iron ore")
            for j in range(0, 16):
                moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])
                if j == 16:
                    time.sleep(2)       
        elif step == 2 and inBank:
                print("Empying coal bag and refilling...")
                moveToCoord(764,500, 2, coords[i][3], "right")
                moveToCoord(689,517, 2, coords[i][3], "left")
                moveToCoord(764,500, 2, coords[i][3], "right")
                moveToCoord(718,518, 2, coords[i][3], "left")

        else:
            moveToCoord(coords[i][0],coords[i][1], coords[i][2], coords[i][3], coords[i][4])  

        if i == len(coords):
            print("Finished banking.")      

def alch():
    print("Alching...")
    coords = getCoords("alch")["coordinates"]

    # move to spell book
    moveToCoord(coords[0][0],coords[0][1], coords[0][2], coords[0][3], coords[0][4])

    # alch 16 times:
    for i in range(16):
        moveToCoord(coords[1][0],coords[1][1], coords[1][2], coords[1][3], coords[1][4])
        moveToCoord(coords[2][0],coords[2][1], coords[2][2], coords[2][3], coords[2][4])

        


def deposit():
    print("Depositing bars...")
    coords = getCoords("deposit")["coordinates"]
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

          
            bank()
            time.sleep(5)
            alch()     
            time.sleep(3)
            deposit()
            time.sleep(4)
            inBank = True
      
                
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)