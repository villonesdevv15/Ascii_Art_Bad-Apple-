# cmd running test
# SEKAI version
import os
import time
import pyautogui  

def run_bad_apple():
    time.sleep(0.5)
    # Updated path for your new folder structure
    os.system("start cmd /k cd C:\\Users\\loren\\OneDrive\\Desktop\\Python\\ASCII Art Program")
    time.sleep(1)
    # Renamed file to avoid issues with '!!'
    pyautogui.write("python SEKAI_VER_Bad_Apple.py", interval=0.1)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey("f11")  # Fullscreen

if __name__ == "__main__":
    run_bad_apple()
