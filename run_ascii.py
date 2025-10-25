# cmd running

import os
import time
import pyautogui  

def run_ascii():
    time.sleep(2)
    # Updated path for your new folder structure
    os.system("start cmd /k cd C:\\Users\\loren\\OneDrive\\Desktop\\Python\\ASCII Art Program")
    time.sleep(1.5)
    # Renamed file to avoid issues with '!!'
    pyautogui.write("python ASCII_Art.py", interval=0.1)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey("f11")  # Fullscreen

if __name__ == "__main__":
    run_ascii()
