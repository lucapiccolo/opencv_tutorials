#import needed libraries
import numpy as np
import cv2

#associate local webcamp as video source
cap = cv2.VideoCapture(0)
#check if capture is initialized - open if needed
if not cap.isOpened():
    cap.open()

while(True):
    ret, frame = cap.read() #capture one frame
    if not ret: #throws error if cannot read frame
        print "Error reading a frame!"
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert frame to grayscale
    cv2.imshow('Webcam', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'): #should avoid problems with numlock
        break

cap.release() #releases the webcam
cv2.destroyAllWindows() #destroys the window
