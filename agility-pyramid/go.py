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
    variation = random.randint(1,1)
    print("Getting agility coords...")
    coordFile = 'laps/coords' + str(variation) + '.json'
    with open(coordFile, 'r') as file:
                loaded_data = json.load(file)
    return loaded_data

def click(t):
    pyautogui.click(button='left')
    time.sleep(t)

def moveToCoord(x, y, time, step):
    print("Coordinate #" + str(step +1) + " x:" + str(x) + " y:" + str(y))
    pyautogui.moveTo(x,y)
    click(time)
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        now = datetime.now()
        timeToRun = now + timedelta(minutes = int(sys.argv[1]) )
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

            for i in range(len(coords)):
                moveToCoord(coords[i][0],coords[i][1], coords[i][2], i)
            
            # print("1st obstacle.")
            # pyautogui.moveTo(coords[0][0], coords[0][1], 0.5)
            # click(5)

            
            # time.sleep(7)
            # print("2nd obstacle.")
            # pyautogui.moveTo(coords[1][0], coords[1][1], 0.5)
            # click(4)

            
            # time.sleep(6)
            # print("3rd obstacle.")
            # pyautogui.moveTo(coords[2][0], coords[2][1], 0.5)
            # click(5)

            
            # time.sleep(5)
            # print("4th obstacle.")
            # pyautogui.moveTo(coords[3][0], coords[3][1], 0.5)
            # click(7)

            
            # time.sleep(7)
            # print("5th obstacle.")
            # pyautogui.moveTo(coords[4][0], coords[4][1], 0.5)
            # click(7)

            # print("6th obstacle.")
            # pyautogui.moveTo(coords[5][0], coords[5][1], 0.5)
            # click(3)

            # print("7th obstacle.")
            # pyautogui.moveTo(coords[6][0], coords[6][1], 0.5)
            # click(3)
            
            # print("8th obstacle.")
            # pyautogui.moveTo(coords[7][0], coords[7][1], 0.5)
            # click(4)

            # print("9th obstacle.")
            # pyautogui.moveTo(coords[8][0], coords[8][1], 0.5)
            # click(5)

            # print("10th obstacle.")
            # pyautogui.moveTo(coords[9][0], coords[9][1], 0.5)
            # click(1)

            # print("11th obstacle.")
            # pyautogui.moveTo(coords[10][0], coords[10][1], 0.5)
            # click(5)

            # print("12th obstacle.")
            # pyautogui.moveTo(coords[11][0], coords[11][1], 0.5)
            # click(6)

            # print("13th obstacle.")
            # pyautogui.moveTo(coords[12][0], coords[12][1], 0.5)
            # click(5)

            # print("14th obstacle.")
            # pyautogui.moveTo(coords[13][0], coords[13][1], 0.5)
            # click(5)

            # print("15th obstacle.")
            # pyautogui.moveTo(coords[14][0], coords[14][1], 0.5)
            # click(5)

            # print("16th obstacle.")
            # pyautogui.moveTo(coords[15][0], coords[15][1], 0.5)
            # click(6)

            # print("17th obstacle.")
            # pyautogui.moveTo(coords[16][0], coords[16][1], 0.5)
            # click(2)

            # print("18th obstacle.")
            # pyautogui.moveTo(coords[17][0], coords[17][1], 0.5)
            # click(3)

            # print("19th obstacle.")
            # pyautogui.moveTo(coords[18][0], coords[18][1], 0.5)
            # click(5)

            # print("20th obstacle.")
            # pyautogui.moveTo(coords[19][0], coords[19][1], 0.5)
            # click(6)

            # print("21st obstacle.")
            # pyautogui.moveTo(coords[20][0], coords[20][1], 0.5)
            # click(7)

            # print("22nd obstacle.")
            # pyautogui.moveTo(coords[21][0], coords[21][1], 0.5)
            # click(8)

            # print("23rd obstacle.")
            # pyautogui.moveTo(coords[22][0], coords[22][1], 0.5)
            # click(2)

            # print("24th obstacle.")
            # pyautogui.moveTo(coords[23][0], coords[23][1], 0.5)
            # click(3)

            # print("25th obstacle.")
            # pyautogui.moveTo(coords[24][0], coords[24][1], 0.5)
            # click(4)

            # print("26th obstacle.")
            # pyautogui.moveTo(coords[25][0], coords[25][1], 0.5)
            # click(3)

            # print("27th obstacle.")
            # pyautogui.moveTo(coords[26][0], coords[26][1], 0.5)
            # click(3)

            # print("28th obstacle.")
            # pyautogui.moveTo(coords[27][0], coords[27][1], 0.5)
            # click(2)

            # print("29th obstacle.")
            # pyautogui.moveTo(coords[28][0], coords[28][1], 0.5)
            # click(1)

            # print("30th obstacle.")
            # pyautogui.moveTo(coords[29][0], coords[29][1], 0.5)
            # click(4)

            # print("31st obstacle.")
            # pyautogui.moveTo(coords[30][0], coords[30][1], 0.5)
            # click(3)

            # print("32nd obstacle.")
            # pyautogui.moveTo(coords[31][0], coords[31][1], 0.5)
            # click(3)

            # print("33rd obstacle.")
            # pyautogui.moveTo(coords[32][0], coords[32][1], 0.5)
            # click(1)

        else:
            print("Ending session at: " + str(datetime.now()))
            logout()
            sys.exit(0)