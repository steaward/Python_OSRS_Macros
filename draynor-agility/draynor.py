import pyautogui
import pynput
import random
import json
import time
import sys
import numpy as np
import cv2
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

# Globals
movementType = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad]
timesToWait = [2, 2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3]
def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1

    return pyautogui.screenshot(region=(x1,y1,width,height))

def moveOnMap(url,x,y, flag, tries):
    print("Moving to better location...")
    pos = imagesearcharea(url, 0,0,800,600,0.5)
    if pos[0] != -1:
        pyautogui.moveTo(pos[0] + x, pos[1] + y, 1.5)
        if flag == True:
                pyautogui.click(button='right')
                time.sleep(1)
                pyautogui.moveTo(pos[0] + x, pos[1] + y + 50, 1.5)
                time.sleep(0.5)
        pyautogui.click(button='left')
        time.sleep(1)
    else: 
        if tries < 3:
                print("Failed to move...trying again")
                resetMap()
                time.sleep(1)
                for i in range (1):
                        tries = tries + 1
                        moveOnMap(url, x,y, flag, tries)
                   
        else:
                teleToBank()
                return  

def imagesearcharea(image, x1,y1,x2,y2, precision=0.8, im=None) :
    
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

def click(t, mouse_button):
    pyautogui.click(button=mouse_button)
    time.sleep(t)


def run():
    with open('coords.json', 'r') as file:
                loaded_data = json.load(file)
    coords = loaded_data["coordinates"]
    # run to first wall
    pyautogui.moveTo(coords[0][0], coords[0][1], 0.5)
    click(4, 'left')
    # click up
    print("Going up:" + str(coords[1][0]) + " " + str(coords[1][1]))
    pyautogui.moveTo(coords[1][0], coords[1][1], 0.5)
    click(5, 'left')
    # first obstacle
    print("First obstacle" + str(coords[2][0]) + " " + str(coords[2][1]))
    pyautogui.moveTo(coords[2][0], coords[2][1], 1)
    click(14, 'left')
    # check for mark
    print("Going to mark #1: " + str(coords[3][0]) + " " + str(coords[3][1]))
    pyautogui.moveTo(coords[3][0], coords[3][1], 2)
    click(3, 'left')
    # second obstacle
    print("Second obstacle: " + str(coords[4][0]) + " " + str(coords[4][1]))
    pyautogui.moveTo(coords[4][0], coords[4][1], 2)
    click(10, 'left')
    # third obstacle
    print("Third obstacle: " + str(coords[5][0]) + " " + str(coords[5][1]))
    pyautogui.moveTo(coords[5][0], coords[5][1], 2)
    click(7, 'left')
    # fourth
    print("Fourth obstacle: " + str(coords[6][0]) + " " + str(coords[6][1]))
    pyautogui.moveTo(coords[6][0], coords[6][1], 2)
    click(4, 'left')
    # fifth
    print("Fifth obstacle: " + str(coords[7][0]) + " " + str(coords[7][1]))
    pyautogui.moveTo(coords[7][0], coords[7][1], 2)
    click(6, 'left')
    print("Going down...")
    pyautogui.moveTo(coords[9][0], coords[9][1], 1)
    click(10, 'left')
    
def reset():
    with open('reset.json', 'r') as file:
                loaded_data = json.load(file)
    coords = loaded_data["coordinates"] 
    # pyautogui.moveTo(coords[0][0], coords[0][1], 0.5)
    # click(4, 'left')
    # pyautogui.moveTo(coords[1][0], coords[1][1], 0.5)
    # click(4, 'left')
    moveOnMap("map.png", coords[0][0], coords[0][1], False,1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
    else:
        print("Please enter a time to run for.")
        sys.exit(0)

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
        if now.minute % 5 == 0:
            reset()
            time.sleep(10)
            run()
        else:
            run()
