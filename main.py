import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")

#Output file name 
filename = "ScreenCaptureMP4.mp4"

#FPS of video
fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
#Window size
cv2.resizeWindow("Live", 380, 270)

#SCREEN RECORD
def Record():
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)

        cv2.imshow("Live", frame)

        #PRESS q to stop recording
        if cv2.waitKey(1) == ord("q"):
            out.release()
            cv2.destroyAllWindows()
            break

Record()
