import cv2
import pygame
video_path = "Bad_Apple!!.mp4"  # video path
audio_path = "Bad_Apple!!.mp3"  # audio path
cap = cv2.VideoCapture(video_path)

# I forgot how to sync in
# audio using pygame
# pygame.mixer.init()
# pygame.mixer.music.load(audio_path)
# pygame.mixer.music.set_volume(1)  # Adjust accordingly (0.0 to 1.0)

# pygame.mixer.music.play()
# Start audio (to sync in with the video) using pygame
if not cap.isOpened():
    print("Could not open the video :( ")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # Reset to the first frame
        ret, frame = cap.read() # Read the first frame again
        if not ret:
            break  # Exit if reading fails even after reset

    cv2.imshow("Bad Apple!!", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'): # Exit if 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()