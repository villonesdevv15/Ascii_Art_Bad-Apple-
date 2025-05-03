# cmd running test
# original version
import os
import time
import pyautogui  

def run_bad_apple():
    time.sleep(0.5)
    os.system("start cmd /k cd C:\\Users\\villo\\OneDrive\\Desktop\\ASCII Art Program")  #C:\\User\Name\\Location\\Document\Folder
    time.sleep(1)
    pyautogui.write("python Bad_Apple!!_ASCII.py", interval=0.1) # run better without after frames
    pyautogui.press("enter") # executing
    time.sleep(0.5)
    pyautogui.hotkey("f11")  # Fullscreen

if __name__ == "__main__":
    run_bad_apple()
