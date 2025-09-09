import keyboard
import webbrowser
import time
import threading
import getpixelcolor

event = threading.Event()

#Function will stop the program from running
def complete():
    event.set()

#Function that will calculate the time when the dino needs to jump
def calculate_jump(enter : float, exit : float) -> float:
    speed = 25/(exit-enter) #pps
    dinoDistance = 1260 - 665
    hitTime = dinoDistance/speed #time until hit

    jumpTime = hitTime - 0.1 #edit second number accordingly as this is the delay it takes the dino to jump

    print(jumpTime)

    return max(jumpTime, 0)
    
#getting in game and starting
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("chrome://dino", new=1)
time.sleep(2)
keyboard.write("Chrome://dino")
keyboard.press_and_release('enter')
time.sleep(1) 
keyboard.press_and_release('space')
        
#Game logic
time_stack1 = []
time_stack2 = []
keyboard.add_hotkey("ctrl+c", complete)
while event.is_set() == 0:
    colors = getpixelcolor.average(1260,300,25,25)
    avg = (colors[0] + colors[1] + colors[2])/3

    if (avg > 40):
        time_stack1.append(time.time())
    elif len(time_stack1)>len(time_stack2):
        time_stack2.append(time.time())
        delay = calculate_jump(time_stack1.pop(0),time_stack2.pop(0))
        threading.Timer(delay, keyboard.press_and_release("Space")).start()

    time.sleep(0.001)






