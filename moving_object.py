
# moving object detection

import cv2
import time
import imutils

cam = cv2.VideoCapture(0)  # initialize the default camera (change index if needed)
time.sleep(1)

firstFrame = None
area = 800  # threshold for noticeable change in movement

while True:
    ret, img = cam.read()
    if not ret:
        break

    text = "Normal"  # no moving object detected

    # pre-processing
    img = imutils.resize(img, width=500)  # resize frame to 500
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to gray scale
    gaussian_img = cv2.GaussianBlur(gray_img, (21, 21), 0)  # smoothening

    if firstFrame is None:  # save the first frame
        firstFrame = gaussian_img
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussian_img)
    thresh_img = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    thresh_img = cv2.dilate(thresh_img, None, iterations=2)  # removes image particles

    conts = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = imutils.grab_contours(conts)

    for c in conts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # src, startpoint, endpoint, color, thickness
        text = "Moving Object Detected"
    print(text)

    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 225), 2)  # (src, text, position, font, fontSize, color, thickness)

    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
