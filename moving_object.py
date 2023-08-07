
# moving object detection

import cv2
import time
import imutils

cam = cv2.VideoCapture(2) #initialize the camera
time.sleep(1)

firstFrame=None
area = 800 # threshold for noticeable change in movement

while True:
    _,img = cam.read()
    text = "Normal" # no moving object detected

    #pre-processing
    img = imutils.resize(img, width=500) # resize frame to 500
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray scale
    gaussian_img = cv2.GaussianBlur(gray_img, (21,21), 0) # smoothening

    if firstFrame is None: #save the first frame
        firstFrame = gaussian_img
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussian_img)
    thresh_img = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    
