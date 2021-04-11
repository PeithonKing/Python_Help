import pyautogui
from PIL import Image, ImageGrab

def press(key):
    pyautogui.keyDown(key)
    return

def detection(picinfo):
    
    # Draw a square to detect night
    for i in range(600,610):
        for j in range(600,610):
            if picinfo[i, j] > 150: time = "day"
            if picinfo[i, j] < 150: time = "night"
    
    # Draw the rectangle for cactus
    for x in range(150, 390):
        for y in range(375, 450):
            if time == "day":
                if picinfo[x, y] < 86:
                    press("space")
                    return
            if time == "night":
                if picinfo[x, y] > 86:
                    press("space")
                    return

import time
time.sleep(4)

while True:
    image = ImageGrab.grab().convert('L')  
    picinfo = image.load()
    detection(picinfo)
        
    '''
    # Draw the rectangle for cactus
    for x in range(150, 390):
        for y in range(375, 450):
            picinfo[x, y] = 86
            
    # Draw blank space to detect night
    for i in range(600,610):
        for j in range(600,610):
            picinfo[i, j] = 86
            
    image.show()
    break'''
