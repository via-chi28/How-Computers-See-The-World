import cv2
img = cv2.imread("poster.jpg")

#rocket = img[120:360,400:500]
#img[0:240, 500:600] = rocket

cv2.imshow("output", img)
cv2.waitKey(0)

