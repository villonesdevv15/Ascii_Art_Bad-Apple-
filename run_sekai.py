# cmd running test
# SEKAI version
import os
import time
import pyautogui  

def run_bad_apple():
    time.sleep(0.5)
    # Updated path for your new folder structure
    # if lazy do this win + r type cmd and copy paste this cd C:\\Users\\name\\Folder\\Folder\\Folder\\Folder
    os.system("start cmd /k cd C:\\Users\\name\\Folder\\Folder\\Folder\\Folder")
    time.sleep(1)
    # Renamed file to avoid issues with '!!'
    pyautogui.write("python SEKAI_VER_Bad_Apple_ASCII.py", interval=0.1)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey("f11")  # Fullscreen

if __name__ == "__main__":
    run_bad_apple()
