import cv2
vs = cv2.VideoCapture(0) # initialize camera

while True:
    _, img = vs.read()

    cv2.imshow("VideoStream", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") :
        break

vs.release() # release the camera

cv2.destroyAllWindows()
