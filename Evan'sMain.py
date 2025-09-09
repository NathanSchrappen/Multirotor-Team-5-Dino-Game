import keyboard
import webbrowser
import time
import threading
import getpixelcolor

event = threading.Event()

def complete():
    event.set()
    
#getting in game and starting
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("chrome://dino", new=2)
time.sleep(2)
keyboard.write("Chrome://dino")
keyboard.press_and_release('enter')
time.sleep(1) 
keyboard.press_and_release('space')
        

keyboard.add_hotkey("ctrl+c", complete)
while event.is_set() == 0:
    keyboard.press_and_release("space")
    #colors = getpixelcolor.area()
    time.sleep(1)






