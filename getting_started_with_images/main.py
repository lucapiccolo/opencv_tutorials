#import needed libraries
import numpy as np
import cv2

#open image in grayscale mode
img = cv2.imread('C:\\Users\\l.piccolo\\Pictures\\apple.png', cv2.IMREAD_GRAYSCALE)
#show the image and wait for a keyboard keystroke
cv2.namedWindow('Image of an apple', cv2.WINDOW_NORMAL) #create a resizable window
cv2.imshow('Image of an apple', img) #add image to window
key = cv2.waitKey(0) #waits for a keyboard keystroke - needed

#if key pressed is 's', save image, otherwise exit
if key == ord('s'):
    print "Saving as C:\\Users\\l.piccolo\\Pictures\\apple_in_grayscale.png'"
    cv2.imwrite('C:\\Users\\l.piccolo\\Pictures\\apple_in_grayscale.png', img)
    print "Closing..."
    cv2.destroyAllWindows() #closes the window
else:
    print "Closing..."
    cv2.destroyAllWindows() #closes the window
