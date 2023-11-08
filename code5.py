import numpy as np
import cv2

black = np.zero([6,6])
#print(black)
black[2:4,2:4] = 255
print(black)
cv2.imshow("black",black)
cv2.waitKey(0)
