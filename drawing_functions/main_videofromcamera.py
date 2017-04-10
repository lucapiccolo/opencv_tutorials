#import needed libraries
import numpy as np
import cv2

#associate local webcam as video source
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() #capture one frame
    if not ret: #throws error if cannot read frame
        print "Error reading a frame!"
        break

    cv2.line(frame,(0,0),(640,450),(255,0,0),5) #draw line
    cv2.rectangle(frame,(20,20),(100,100),(0,255,0),3) #draw rectangle
    cv2.circle(frame,(60,60),40,(0,0,255),2) #draw circle
    cv2.ellipse(frame,(320,240),(50,25),0,0,360,(255,255,0),4) #draw ellipse
    cv2.putText(frame,'Hello!',(250,250),cv2.FONT_HERSHEY_SIMPLEX,
                4,(255,255,255),3,cv2.LINE_AA) #write 'Hello!'
    
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #should avoid problems with numlock
        break

cap.release() #releases the webcam
cv2.destroyAllWindows() #destroys the window
