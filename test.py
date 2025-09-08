import time

import pyautogui
import getpixelcolor

print("Press Ctrl-C to quit.")

# def detectChromeTheme():
#     match getpixelcolor.pixel(100, 500):
#         case tuple(37, 37, 38):
#             return


#     return getpixelcolor.pixel(100, 500)

pyautogui.press("browserhome")
time.sleep(1)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("chrome://dino")
pyautogui.press(keys="enter")
pyautogui.press("f11")

pyautogui.moveTo(100, 500, duration=0.1)

color = getpixelcolor.pixel(100, 500)

try:
    while True:
        # Get color of outside screen to determine whether it's light or dark mode
        color = getpixelcolor.pixel(100, 500)
        print(print(color), end="")
        print("\b" * len(str(color)), end="", flush=True)
except KeyboardInterrupt:
    print("\n")

print(color)
"""
What this code needs to do:
* Detect when a 
chrome://dino
"""
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#         print(positionStr, end="")
#         print("\b" * len(positionStr), end="", flush=True)
# except KeyboardInterrupt:
#     print("\n")
