# import pyautogui
import pynput
import pyautogui
import random
import time
import sys
import json
import numpy
import keyboard
import numpy as np
import cv2
import datetime

from pynput.mouse import Listener, Button, Controller
from pynput.keyboard import Listener as kbList, Key, Controller as kb
from json import JSONEncoder

##### Classes #####
class AreaOfSuccess:
        def __init__(self, x, y):
                self.coord = { 'x' : x,
                               'y' : y,
                               'found': False
                              }

        def __repr__(self):
                return ''.join(str(self.coord))

        def __dict__(self):
                return dict(self.coord)

class CurrentAction:
        def __init__(self, currentAction):
                self.Action = currentAction

##### Functions #####
### on_x functions are used when script is ran with argument: startup.
### startup argument means we wish to record where we want our program to click

# scrolling mouse wheel up will stop the program from taking any more inputs (kill the program as well...)
# will convert our List<AreaOfSuccess> to JSON and save the data to a JSON file.
def on_scroll(x, y, dx, dy):
        if len(sys.argv) > 1:
                if sys.argv[1] == "teletobank":
                        ## dump our areaOfSuccesses (2D array) to JSON
                        print("Data before serialization: " + str(areaOfSuccesses))
                        serialized = array2DtoJson(areaOfSuccesses)
                        with open('tele_coords.json', 'w') as json_file:  
                              json.dump(serialized, json_file)

                if sys.argv[1] == "bank":
                        ## dump our areaOfSuccesses (2D array) to JSON
                        print("Data before serialization: " + str(areaOfSuccesses))
                        serialized = array2DtoJson(areaOfSuccesses)
                        with open('bank_coords.json', 'w') as json_file:  
                              json.dump(serialized, json_file)

                if sys.argv[1] == "startup":
                        ## dump our areaOfSuccesses (2D array) to JSON
                        print("Data before serialization: " + str(areaOfSuccesses))
                        serialized = array2DtoJson(areaOfSuccesses)
                        with open('iron_mining_coords_mon.json', 'w') as json_file:  
                              json.dump(serialized, json_file)\

                if sys.argv[1] == "drop":
                        ## dump our areaOfSuccesses (2D array) to JSON
                        print("Data before serialization: " + str(areaOfSuccesses))
                        serialized = array2DtoJson(areaOfSuccesses)
                        with open('drop_coords.json', 'w') as json_file:  
                              json.dump(serialized, json_file)
                 
        pynput.mouse.Listener.StopException
        return False

# left click:  record coord
# right click: jump to next 'area of success' we want to record coords for
def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.left or button == Button.right:
                print("Adding coords " + str(x) + ", " + str(y) + " to current action # " + str(currentAction.Action + 1))
                areaOfSuccesses[currentAction.Action].append(AreaOfSuccess(x,y))
        if button == Button.middle:
                if (currentAction.Action == 2):
                        currentAction.Action = 0
                else:
                        currentAction.Action += 1

## End of clicking functions

## json conversion functions:
def array2DtoJson(arr):
        s = '{"' + 'areaOfSuccesses' + '":['
        # newLine = '\n'
        for i in range(len(arr)):
             s += array1DtoJson(arr[i])       
             if i < (len(arr) -1):
                     s += ','
        s+= ']}'  
        return s

def array1DtoJson(arr): 
        s = '['
        for i in range (len(arr)):
                s += str(arr[i].coord)
                if i < (len(arr) -1):
                     s += ','
        s += ']'
        return s

#end of Json conversion functions

# CV helpers:
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

def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1

    return pyautogui.screenshot(region=(x1,y1,width,height))

def clickObstacle(obstacleNumber, x, y,bool):
    clickSpeed = random.randint(0,3)
    if bool == True:
        imageURL = "obstacle" + str(obstacleNumber) + "a" + ".png"
    else:
        imageURL = "obstacle" + str(obstacleNumber) + ".png"

    print ("Gathering image... " + imageURL)
    im = region_grabber((0, 0, 800, 600))
    pos = imagesearcharea(imageURL, 0,0,800,600,0.4)
    time.sleep(1)
    if pos[0] != -1:
        pyautogui.moveTo(pos[0] + x, pos[1] + y, clickSpeed)
        pyautogui.click(button='left')
        return True
    return False

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
# encd of CV helpers

def clickTeleTab():
     x = random.randint(622,626)
     y = random.randint(254,258)
     pyautogui.click(x, y)


def isSubSet(A,B):
    n=-1
    while True:
        try:
            n = A.index(B[0],n+1)
        except ValueError:
            return False
        if A[n:n+len(B)]==B:
            return True

def on_pressKey(key):
        print(str(key) + " hit.")

def dropItems():
        print("Starting to drop resources...") 
        with open('drop_coords.json', 'r') as file:
                loaded_data = json.load(file)

        # for some reason, json.loads needs to see " instead of ' in our dict object
        loaded_data = loaded_data.replace("'", "\"")

                # fill data
        loaded_data = json.loads(loaded_data)
        numberOfActions = 0
        for i in loaded_data.values():
                for d in i:
                        numberOfActions += 1
                        data = [[] * i for i in range(numberOfActions)]

                for d in loaded_data.values():
                        # action found here:
                        actionValue = 0
                        for action in d:
                                # coords found here:
                                for i in range(0,len(action)):
                                        coord = action[i]
                                        if coord.values() is not None:
                                                data[actionValue].append(AreaOfSuccess(coord['x'], coord['y']))
                                        if i == (len(action) - 1):
                                                actionValue += 1

        seenCoords = [[] * len(data) for i in range(len(data) + 1)]
        currentAction = CurrentAction(0)
        clickCount = 0
        while True:
                print("Main function starting up...")
                # randomly choose which one to drop:
                # we do not need to track current action, rather just make sure we don't go over 27 unique clicks...
                # remeber the ones in which we've dropped
                randomAction = random.randint(0, len(data)-1)
                arrayOfCoords = data[randomAction]
                randomClick = random.randint(0, (len(arrayOfCoords)-1))

                
                if not seenCoords[randomAction]:
                        ## do it
                        if len(arrayOfCoords) != 0:
                                randomTimeToMoveMouse = random.uniform(0, 0.5)
                                y = arrayOfCoords[randomClick].coord['y']
                                x = arrayOfCoords[randomClick].coord['x']
                                print("Moving to location in current action: " + str(currentAction.Action + 1) + " location: " + str(arrayOfCoords[randomClick]))
                                keyboard.press('shift')
                                pyautogui.moveTo(x, y, randomTimeToMoveMouse)
                                time.sleep(randomTimeToMoveMouse + 0.3)
                                pyautogui.click()
                                time.sleep(0.1)
                                pyautogui.click()
                                keyboard.release('shift')
                                clickCount += 1
                                arrayOfCoords[randomClick].coord['found'] = True
                                seenCoords[randomAction].append(arrayOfCoords)
                                if currentAction.Action == (numberOfActions - 1):
                                        currentAction.Action = 0
                                else:
                                        currentAction.Action += 1

                                if clickCount == 27:
                                        keyboard.release('shift')
                                        return
                elif not seenCoords[randomAction][randomClick][0].coord['found']:
                         ## do it
                        if len(arrayOfCoords) != 0:
                                randomTimeToMoveMouse = random.uniform(0, 0.3)
                                y = arrayOfCoords[randomClick].coord['y']
                                x = arrayOfCoords[randomClick].coord['x']
                                print("Moving to location in current action: " + str(currentAction.Action + 1) + " location: " + str(arrayOfCoords[randomClick]))
                                keyboard.press('shift')
                                pyautogui.moveTo(x, y, randomTimeToMoveMouse)
                                time.sleep(randomTimeToMoveMouse + 0.3)
                                pyautogui.click()
                                time.sleep(0.1)
                                pyautogui.click()
                                keyboard.release('shift')
                                clickCount += 1
                                arrayOfCoords[randomClick].coord['found'] = True
                                seenCoords[randomAction].append(arrayOfCoords)
                                if currentAction.Action == (numberOfActions - 1):
                                        currentAction.Action = 0
                                else:
                                        currentAction.Action += 1

                                if clickCount == 27:
                                        keyboard.release('shift')
                                        return
def bankItems():
        print("Starting to bank items...")
        with open('bank_coords.json', 'r') as file:
                loaded_data = json.load(file)

        # for some reason, json.loads needs to see " instead of ' in our dict object
        loaded_data = loaded_data.replace("'", "\"")

                # fill data
        loaded_data = json.loads(loaded_data)
        numberOfActions = 0
        for i in loaded_data.values():
                for d in i:
                        numberOfActions += 1
                        data = [[] * i for i in range(numberOfActions)]

                for d in loaded_data.values():
                        # action found here:
                        actionValue = 0
                        for action in d:
                                # coords found here:
                                for i in range(0,len(action)):
                                        coord = action[i]
                                        if coord.values() is not None:
                                                data[actionValue].append(AreaOfSuccess(coord['x'], coord['y']))
                                        if i == (len(action) - 1):
                                                actionValue += 1
        currentAction = CurrentAction(0)
        clickCount = 0
        ## scroll all the way out
        pyautogui.scroll(20)
        moveOnMap("minimap.png",140, 110,False,1)
        time.sleep(0.5)
        while True:
                arrayOfCoords = data[currentAction.Action]
                if len(arrayOfCoords) != 0:
                        randomClick = random.randint(0, (len(arrayOfCoords)-1))
                        randomTimeToMoveMouse = random.uniform(0.5, 1.5)
                        y = arrayOfCoords[randomClick].coord['y']
                        x = arrayOfCoords[randomClick].coord['x'] - 5
                        print("Moving to location in current action: " + str(currentAction.Action + 1) + " location: " + str(arrayOfCoords[randomClick]))
                        if clickCount == 0:
                                pyautogui.moveTo(x, y, randomTimeToMoveMouse)
                                time.sleep(randomTimeToMoveMouse + 1)
                                pyautogui.click()
                        
                        else:
                                pyautogui.moveTo(x, y, randomTimeToMoveMouse)
                                time.sleep(0.5)
                                pyautogui.click() 
                        # if (randomTimeToMoveMouse > 1):
                        #         time.sleep(0.1)
                        #         pyautogui.click()
                        time.sleep(randomTimeToMoveMouse + 0.5)
                        clickCount += 1
                        if currentAction.Action == (numberOfActions - 1):
                                currentAction.Action = 0
                        else:
                                currentAction.Action += 1
                        
                        if clickCount == 6:
                        ## scroll equal amounts back
                                pyautogui.scroll(-20)
                                return
        return

def teleToBank():
        print("Teleing to bank...")
        with open('tele_coords.json', 'r') as file:
                loaded_data = json.load(file)

        # for some reason, json.loads needs to see " instead of ' in our dict object
        loaded_data = loaded_data.replace("'", "\"")

                # fill data
        loaded_data = json.loads(loaded_data)
        numberOfActions = 0
        for i in loaded_data.values():
                for d in i:
                        numberOfActions += 1
                        data = [[] * i for i in range(numberOfActions)]

                for d in loaded_data.values():
                        # action found here:
                        actionValue = 0
                        for action in d:
                                # coords found here:
                                for i in range(0,len(action)):
                                        coord = action[i]
                                        if coord.values() is not None:
                                                data[actionValue].append(AreaOfSuccess(coord['x'], coord['y']))
                                        if i == (len(action) - 1):
                                                actionValue += 1
        currentAction = CurrentAction(0)
        clickCount = 0

        
        
        while True:
                arrayOfCoords = data[currentAction.Action]
                if len(arrayOfCoords) != 0:
                        randomClick = random.randint(0, (len(arrayOfCoords)-1))
                        randomTimeToMoveMouse = random.uniform(0.5, 1.5)
                        y = arrayOfCoords[randomClick].coord['y']
                        x = arrayOfCoords[randomClick].coord['x']
                        print("Moving to location in current action: " + str(currentAction.Action + 1) + " location: " + str(arrayOfCoords[randomClick]))
                        pyautogui.moveTo(x, y, randomTimeToMoveMouse)
                        if clickCount == 0:
                                pyautogui.click(button='right')
                        else:
                                pyautogui.click()
                        # if (randomTimeToMoveMouse > 1):
                        #         time.sleep(0.1)
                        #         pyautogui.click()
                        time.sleep(randomTimeToMoveMouse + 0.5)
                        clickCount += 1
                        if currentAction.Action == (numberOfActions - 1):
                                currentAction.Action = 0
                        else:
                                currentAction.Action += 1
                        
                        if clickCount == 3:
                                #teleToMonestary()
                                return

def resetMap():
    print("Reseting the map...")
    pos = imagesearcharea("reset.png", 0,0,800,600,0.5)
    if pos[0] != -1:
        pyautogui.moveTo(pos[0] +20, pos[1] + 20, 1.5)
        pyautogui.click(button='left')

def teleToMonestary():
#        pyautogui.click(685, 208) 
#        time.sleep(0.5)
#        pyautogui.click(210, 288)
#        time.sleep(0.6)
#        pyautogui.click(597, 329)
#        time.sleep(0.4)
#        resetMap()
#        time.sleep(0.5)
       moveOnMap("monestary.png", 110, 50, False,1)
       time.sleep(3)
       moveOnMap("monestary_rocks.png", 20, 30, False,1)

def returnToMines():
        clickTeleTab()
        time.sleep(2)
        moveOnMap("ardy_1.png",170, 90, False,1)
        time.sleep(3.5)
        moveOnMap("ardy_2a.png",170, 50, False,1)
        time.sleep(5)
        moveOnMap("ardy_3.png",170, 25, False,1)
        time.sleep(5)
        #moveOnMap("ardy_3a.png",250, 250, False)
        time.sleep(3)
        moveOnMap("rocks_1.png", 79, 63, True,1)
        return
# !---- MAIN program: -----! #

if __name__ == '__main__':
        ## execute logic to record mouse clicks
        if len(sys.argv) > 1:
                 if sys.argv[1] == "startup" or sys.argv[1] == "teletobank" or sys.argv[1] == 'bank':
                        print("Gathering mouse data...")
                        n = 4 # to-do: make this a command line argument
                        currentAction = CurrentAction(0)
                        areaOfSuccesses = [[] * n for i in range(n)] 
                        with pynput.mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
                                listener.join()
                 if sys.argv[1] == "drop":
                         print("Gathering drop data...")
                         n = 27 # to-do: make this a command line argument
                         currentAction = CurrentAction(0)
                         areaOfSuccesses = [[] * n for i in range(n)] 
                         with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
                                 listener.join()
        ## start the bot.
        else:
             time.sleep(5)
             teleToBank()
             time.sleep(5)
             bankItems()
             time.sleep(3)
             #clickTeleTab()
             time.sleep(2)
             returnToMines()
             time.sleep(2)
             resetMap()
             print("Starting to mine resources...") 
             with open('iron_mining_coords.json', 'r') as file:
                loaded_data = json.load(file)

             # for some reason, json.loads needs to see " instead of ' in our dict object
             loaded_data = loaded_data.replace("'", "\"")

             # fill data
             loaded_data = json.loads(loaded_data)
             numberOfActions = 0
             for i in loaded_data.values():
                     for d in i:
                        numberOfActions += 1
             print(numberOfActions)
             data = [[] * i for i in range(numberOfActions)]

             for d in loaded_data.values():
                # action found here:
                actionValue = 0
                for action in d:
                        # coords found here:
                        for i in range(0,len(action)):
                                coord = action[i]
                                if coord.values() is not None:
                                        data[actionValue].append(AreaOfSuccess(coord['x'], coord['y']))
                                if i == (len(action) - 1):
                                        actionValue += 1
             currentAction = CurrentAction(0)
             clickCount = 0
             # pick a coord from the proper action.
             while True:
                arrayOfCoords = data[currentAction.Action]
                if len(arrayOfCoords) != 0:
                        randomClick = random.randint(0, (len(arrayOfCoords)-1))
                        randomTimeToMoveMouse = random.uniform(0.5, 4)
                        y = arrayOfCoords[randomClick].coord['y']
                        x = arrayOfCoords[randomClick].coord['x']
                        print("Moving to location in current action: " + str(currentAction.Action + 1) + " location: " + str(arrayOfCoords[randomClick]))
                        pyautogui.moveTo(x, y, randomTimeToMoveMouse)
                        pyautogui.click()
                        if (randomTimeToMoveMouse > 1):
                                time.sleep(0.1)
                                pyautogui.click()
                        time.sleep(randomTimeToMoveMouse + 0.5)
                        clickCount += 1
                        if currentAction.Action == (numberOfActions - 1):
                                currentAction.Action = 0
                        else:
                                currentAction.Action += 1

                        if clickCount == 27:
                                endTime = datetime.datetime(2019,7,29,13,0,0)
                                if datetime.datetime.now() > endTime:
                                        break
                                clickCount = 0
                                # #dropItems()
                                # teleToBank()
                                # time.sleep(3)
                                # bankItems()
                                # returnToMines()
                                # time.sleep(3)
                                # resetMap()
                                #      teleToBank()
                                teleToBank()
                                time.sleep(5)
                                bankItems()
                                time.sleep(3)
                                #clickTeleTab()
                                #time.sleep(2)
                                returnToMines()
                                time.sleep(2)
    

             


