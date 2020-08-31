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
import cv2
import numpy as np
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]

def getCoords(type):
    if type == "course":
        # variation = random.randint(1,1)
        variation = 2
        print("Getting agility coords...")
        coordFile = 'laps/coords' + str(variation) + '.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

    if type == "sell":
        print("Getting agility coords...")
        coordFile = 'sell.json'
        with open(coordFile, 'r') as file:
                    loaded_data = json.load(file)
        return loaded_data

def click(t):
    pyautogui.click(button='left')
    time.sleep(t)

def moveToCoord(x, y, time, step):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y) + "run time: " +str(time))
    pyautogui.moveTo(x,y)
    if (step == 30):
        click(2)

    click(time + delay)
    
def sellTokens():
    coords = getCoords("sell")

# IMAGE SEARCH FUNCTIONS 
def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1

    return pyautogui.screenshot(region=(x1,y1,width,height))

def imagesearcharea(image, x1,y1,x2,y2, precision=0.8, im=None) :
    print("Searcing for area")
    if im is None :
        im = region_grabber(region=(x1, y1, x2, y2))
        im.save('testarea.png')

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


def click_from_image(imageURL, area = None):
    print ("Gathering image... " + imageURL)
    im = region_grabber((10, 10, 400, 300))
    pos = imagesearcharea(imageURL, 0,0,800,600,0.8,area)
    time.sleep(1)
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click(button='left')
        return True
    return False  

def findTokenGuy(attempt):
    if attempt > 0:
        attempt = 0
    print("Finding token guy attemp: " + str(attempt))
    guy = 'dude/guy' + str(attempt) + '.png'
    area = 'sellArea.png'
    
    success = click_from_image(guy)

    if not success:
        attempt = attempt + 1
        print ("Failed to find guy.")
        time.sleep(1)
        findTokenGuy(attempt)

    print(str(success))

def sellTokens():
    coords = getCoords("sell")["coordinates"]
    for i in range(len(coords)):
        moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
    print("Selling tokens")
    findTokenGuy(0)
    time.sleep(18000)

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

    print("Starting pyramid plunder!")
    laps = 0
    while True:
        now = datetime.now()

        if laps == 3:
            sellTokens()

        if now < timeToRun:
            # every 15 minutes, take a break (33% of the time)
            if now.minute % 15 == 0:
                factor = random.randrange(1,15)
                if factor == 3:
                    print("Taking a break...")
                    time.sleep(random.randrange(60,120))

            print("Running at current time: " + str(datetime.now()) + " Time to end: " + str(timeToRun))
            moveType = random.choice(movementType)

            coords = getCoords("course")["coordinates"]
            # MOVE
            print("Lap: " + str(laps))
            if laps == 1 and startingCoord != 0:
                startingCoord = 0

            for i in range(startingCoord, len(coords)):
                
                if i == 0:
                    time.sleep(5)

                if i == 4:
                    time.sleep(1)    
                
                if i == len(coords):
                    print("Last lap!")

                if coords[i][3] == False:
                    moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)       
                else:
                    done = False; 
                    if i < 20:
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
                        while(not done):
                            second = datetime.now().second
                            if (second > 9):
                                second = second % 10
                        
                            if (second % 3 == 0):
                                moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
                                done = True;
                            else:
                                print("Not moving...not time yet." + str(second))
                                time.sleep(0.5)

                
            laps = laps + 1  
                
        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)