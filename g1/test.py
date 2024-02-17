import cv2

import numpy as np

img = cv2.imread("cv2_g1_g2/put.jpg")
# img = cv2.resize(img)

# img [100:150, 300:300] = 193, 149, 68
# cv2.rectangle(img, (30,70), (100,100), (255,100,50), thickness=1)
# cv2.rectangle(img, (30,70), (100,100), (255,150,100), thickness=1)
# cv2.rectangle(img, (30,70), (200,200), (255,100,50), thickness=1)
# cv2.circle(img, (250,250), 250, (0,255,0))
cv2.imshow("IMG", img)
cv2.waitKey(0)