import numpy as np
import cv2

black = np.zero([6,6])
#print(black)
f_row = black[1:2]
print(f_row)

f_col = black[:,1:2]
print(f_col)
#cv2.imshow("black",black)
#cv2.waitKey(0)
