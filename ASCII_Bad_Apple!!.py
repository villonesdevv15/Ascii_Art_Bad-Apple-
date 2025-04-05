# Original Sources:
# https://www.youtube.com/watch?v=FtutLA63Cp8&ab_【東方】Bad Apple!! ＰＶ【影絵】
# https://www.youtube.com/watch?v=v-fc1zv31zE&ab_ Bad Apple!! feat.SEKAI / 25時、ナイトコードで。 × 初音ミク

# Ascii art for both Bad Apple!! and Bad Apple!! (SEKAI version)

import cv2
import numpy as np
import time
import os
import pygame

# ASCII characters 
ASCII_CHARS = '  .:-=+*#%@' # ascii_chars 
# Other ASCII char (alternative)
    # '  .,:;+*&%@#$' for Bad Apple!! feat.SEKAI (SEKAI version)
    # ' $8obdpq0L@n1+"`' for Bad Apple!! (Original version)
    # ' @#S%?*+;:,.' alternative

# Video path for capture
video_path = "SEKAI_Bad_apple!!.mp4" # change mp4 file path for different versions of Bad Apple!!
audio_path = "SEKAI_Bad_apple!!.mp3" # change mp3 file path for different versions of Bad Apple!!

cap = cv2.VideoCapture(video_path)

# Output width
OUTPUT_WIDTH = 150  # terminal size (make sure to scroll the terminal to the top for full view 
                                    # or else you can't see the whole thing)
fps = cap.get(cv2.CAP_PROP_FPS) 
frame_time = 1 / fps  # Time per frame 

# audio using pygame
pygame.mixer.init()
pygame.mixer.music.load(audio_path)

# Function to convert the frame to ASCII 
def frame_to_ascii(frame, width=OUTPUT_WIDTH):
    height, orig_width = frame.shape
    aspect_ratio = orig_width / height
    new_height = int(width / aspect_ratio * 0.5)  # height scaling
    resized_frame = cv2.resize(frame, (width, new_height))

    ascii_frame = "\n".join(
        "".join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in row)
        for row in resized_frame
    )
    return ascii_frame

# Start audio (to sync in with the video) using pygame
pygame.mixer.music.play()
start_time = time.time()  # time tracking (making sure every frame counts)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Video ends 
                # If complete scroll down the terminal
    # Convert frame to grayscale (hahaha)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert to ASCII
    ascii_art = frame_to_ascii(gray_frame)

    # Clear screen and print ASCII frame 
    # If the screen flashes abnormally make adjustments
    os.system("cls" if os.name == "nt" else "clear")  # Windows: cls
    print(ascii_art)

    # Sync with audio
    frame_count += 1
    expected_time = start_time + (frame_count * frame_time)
    sleep_time = max(0, expected_time - time.time())  # no negative 
    time.sleep(sleep_time)

# Cleanup
cap.release()
pygame.mixer.music.stop()
