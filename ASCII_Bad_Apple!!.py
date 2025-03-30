
import cv2
import numpy as np
import time
import os
import pygame

# ASCII characters 
ASCII_CHARS = '  .:-=+*#%@' # ASCII_CHARS
# Other ASCII char for every VERSION
    # '  .:-=+*#%@' ascii_char for Bad Apple!! feat.SEKAI (SEKAI version)
    # ' $8obdpq0L@n1+"`' ascii_char for Bad Apple!! 

video_path = "SEKAI_Bad_apple!!.mp4"
audio_path = "SEKAI_Bad_apple!!.mp3"
cap = cv2.VideoCapture(video_path)
OUTPUT_WIDTH = 150
fps = cap.get(cv2.CAP_PROP_FPS)
frame_time = 1 / fps
pygame.mixer.init()
pygame.mixer.music.load(audio_path)

def frame_to_ascii(frame, width=OUTPUT_WIDTH):
    height, orig_width = frame.shape
    aspect_ratio = orig_width / height
    new_height = int(width / aspect_ratio * 0.5)
    resized_frame = cv2.resize(frame, (width, new_height))

    ascii_frame = "\n".join(
        "".join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in row)
        for row in resized_frame
    )
    return ascii_frame

pygame.mixer.music.play()
start_time = time.time()
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_art = frame_to_ascii(gray_frame)
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_art)
    frame_count += 1
    expected_time = start_time + (frame_count * frame_time)
    sleep_time = max(0, expected_time - time.time())
    time.sleep(sleep_time)
cap.release()
pygame.mixer.music.stop()
