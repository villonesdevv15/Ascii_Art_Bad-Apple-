# test video for comparison
import cv2
import pygame
import time

video_path = "Bad_Apple!!.mp4"
audio_path = "Bad_Apple!!.mp3"

# Initialize video capture
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Could not open the video :(")
    exit()

# Get video properties for sync
fps = 30
frame_delay = 1.0 / fps

# Initialize audio
pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.set_volume(1.0)

# Start both at the same time
audio_start_time = time.time() + 0.2  # Small delay to account for initialization
pygame.mixer.music.play(start=0.0)
video_start_time = audio_start_time

while True:
    # Calculate proper frame display time
    current_time = time.time()
    expected_frame_time = (current_time - video_start_time)
    
    ret, frame = cap.read()
    if not ret:
        break
    
    # Show frame
    cv2.imshow("Bad Apple!!", frame)
    
    # Calculate the time to wait for the next frame
    frame_pos = cap.get(cv2.CAP_PROP_POS_FRAMES)
    target_time = video_start_time + (frame_pos / fps)
    wait_time = max(1, int((target_time - time.time()) * 1000))
    
    # Exit on the '/' key or window close
    if cv2.waitKey(wait_time) & 0xFF == ord('/') or cv2.getWindowProperty("Bad Apple!!", cv2.WND_PROP_VISIBLE) < 1:
        break

pygame.mixer.music.stop()
cap.release()
cv2.destroyAllWindows()
