import pyautogui
import pynput
import datetime
from pynput.mouse import Listener, Button, Controller

def on_click(x, y, button, pressed):
    if pressed:
        endTime = datetime.datetime(2019,7,29,4,0,0)
        if datetime.datetime.now() > endTime:
            if button == Button.left:
                x, y = pyautogui.position()
                print(str(x) + "," + str(y))

        if button == Button.middle:
            pynput.mouse.Listener.StopException
            return False


if __name__ == '__main__':
    try:
        with pynput.mouse.Listener(on_click=on_click) as listener:
                            listener.join()  
    except KeyboardInterrupt:
        print('\nDone.')