#import needed libraries
import numpy as np
import cv2

#associate local file as video source
cap = cv2.VideoCapture("C:\\Users\\l.piccolo\\Videos\\snowflake.avi")
#check if capture is initialized
if not cap.isOpened():
    print "Couldn't open!"

while(True):
    ret, frame = cap.read() #capture one frame
    if not ret: #throws error if cannot read frame
        print "Error reading a frame!"
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert frame to grayscale
    cv2.imshow('Video playback', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'): #should avoid problems with numlock
        break

cap.release() #releases the video source
cv2.destroyAllWindows() #destroys the window
