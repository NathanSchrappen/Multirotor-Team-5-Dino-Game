import keyboard
import webbrowser
import time
import threading
import getpixelcolor
from PIL import ImageDraw, ImageGrab

event = threading.Event()

#Variables
xCord = 1260
yCord = 300
xBuf = 50
yBuf = 25

dinoXCord = 665

averageCieling = 40

currJump = None
lastJump = currJump

################################################### FUNCTIONS ################################################### 

#literally jumps
def Jump():
    keyboard.press_and_release("space")
    currJump = time.time()
    lastJump = currJump

#take Image for debugging purposes to visualize where box is
def takeImage():
    pic = ImageGrab.grab()
    draw = ImageDraw.Draw(pic)
    draw.rectangle([xCord,yCord,xCord+xBuf,yCord+yBuf], outline="red", width=3)
    pic.show()

#Function will stop the program from running         
def complete():
    event.set()                          

#Function that will calculate the time when the dino needs to jump
def calculate_jump(enter : float, exit : float) -> float:
    speed = xBuf/(exit-enter) #pps
    dinoDistance = xCord - dinoXCord
    hitTime = dinoDistance/speed #time until hit

    print(speed)
    dinoJumpDeb = max(0, 1 - (speed / 1200))
    jumpTime = hitTime - dinoJumpDeb - (currJump - lastJump)

    print(jumpTime)

    return max(jumpTime, 0)
    
################################################### MAIN ################################################### 

#getting in game and starting         
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("chrome://dino")
time.sleep(2)              
keyboard.write("Chrome://dino")
keyboard.press_and_release('enter')
time.sleep(1) 
Jump()

#Game logic
time_stack1 = []
time_stack2 = []
keyboard.add_hotkey("ctrl+c", complete)
while event.is_set() == 0:
    colors = getpixelcolor.average(xCord,yCord,xBuf,yBuf)
    avg = (colors[0] + colors[1] + colors[2])/3

    if (avg > averageCieling and not len(time_stack1) > len(time_stack2)):
        time_stack1.append(time.time())
    elif (avg <= averageCieling and len(time_stack1)>len(time_stack2)):
        print("JUMP FOR TREE: " + str(avg))
        #takeImage()
        time_stack2.append(time.time())
        delay = calculate_jump(time_stack1.pop(0),time_stack2.pop(0))
        threading.Timer(delay, lambda: Jump()).start()

        time_stack1.clear()
        time_stack2.clear()






