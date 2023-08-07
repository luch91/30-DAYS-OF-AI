import cv2
import imutils

img = cv2.imread("Oluchi.jpg")

cv2.imwrite("OluchiCopy.png",img) # save image as png

cv2.imshow("AI_Master_Class", img)



gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grey

cv2.imwrite("Oluchi_gray.png", gray_img)

cv2.imshow("Orig", img)
cv2.imshow("Gray", gray_img)

# convert threshhold image(black and white)

thresh_img = cv2.threshold(gray_img, 190,255, cv2.THRESH_BINARY)[1]
cv2.imwrite("Oluchi_threshold.jpg", thresh_img)

thresh_img2 = cv2.threshold(gray_img, 100,255, cv2.THRESH_BINARY)[1]
cv2.imwrite("Oluchi_threshold2.jpg", thresh_img2)

thresh_img3 = cv2.threshold(gray_img, 90,255, cv2.THRESH_BINARY)[1]
cv2.imwrite("Oluchi_threshold3.jpg", thresh_img3)

thresh_img4 = cv2.threshold(gray_img, 60,255, cv2.THRESH_BINARY)[1]
cv2.imwrite("Oluchi_threshold4.jpg", thresh_img4)

thresh_img5 = cv2.threshold(gray_img, 75,255, cv2.THRESH_BINARY)[1]
cv2.imwrite("Oluchi_threshold5.jpg", thresh_img5)


# resize an image
resize_img = imutils.resize(img, width=50)
cv2.imwrite("Oluchi_resized.jpg", resize_img)

#image smoothening/ blurring

# dst = cv2.GuassianBlur(src, (kernel), borderType)

guaassian_blur_img = cv2.GaussianBlur(img,(21,21),0)

cv2.imwrite("Oluchi_blur.jpg",guassian_blur_img)



cv2.waitKey(0)

cv2.destroyAllWindows()
