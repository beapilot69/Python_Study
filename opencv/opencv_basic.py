import cv2
import numpy as np
from cv2 import cv2

img_basic = cv2.imread('C:/project/yoon.jpg', cv2.IMREAD_COLOR)

#cv2.namedWindow('Show Image')
cv2.imshow('Image Basic', img_basic)

cv2.waitKey(0)

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)

cv2.destroyAllWindows()

#cv2.imwrite('savedimage.jpg', img_gray)