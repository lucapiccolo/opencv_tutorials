#import needed libraries
import numpy as np
import cv2

#associate local webcam as video source
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('C:\\Users\\l.piccolo\\Videos\\outputVideo.avi',fourcc,20.0,(640,480))

if not cap.isOpened():
    print "Could not open camera!"
if not out.isOpened():
    print "Could not open output stream!"

while(True):
    ret, frame = cap.read() #capture one frame
    if not ret: #throws error if cannot read frame
        print "Error reading a frame!"
        break
    else:
        flipped_frame = cv2.flip(frame,1) #flip vertically
        cv2.imshow('Webcam', flipped_frame) #show flipped frame
        out.write(flipped_frame) #write it to output video
        if cv2.waitKey(1) & 0xFF == ord('q'): #should avoid problems with numlock
            break

cap.release() #releases the webcam
out.release() #release the output video
cv2.destroyAllWindows() #destroys the window
