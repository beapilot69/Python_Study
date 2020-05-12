import numpy as np
import cv2
from cv2 import cv2
from matplotlib import pyplot as plt

# drawing line
img = np.zeros((512,512,3), np.uint8)
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# drawing rectangle
img2 = cv2.rectangle(img,(384,0),(510,128),(255,0,0),3)

# drawing circle
img3 = cv2.circle(img2,(447,63),63,(0,225,0),-1)

# drawing ellipse
img4 = cv2.ellipse(img3,(256,256),(100,50),0,0,180,255,-1)

# adding text to images
font = cv2.FONT_HERSHEY_SIMPLEX
img6 = cv2.putText(img4, 'OpenCV', (10,500),font,4,(255,255,255),2,cv2.LINE_AA)

plt.imshow(img[:,:,::-1])
plt.imshow(img2[:,:,::-1])
plt.imshow(img3[:,:,::-1])
plt.imshow(img4[:,:,::-1])
plt.imshow(img6[:,:,::-1])
plt.show()

# git 공부를 위한 각주 추가