import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

   success, img = cap.read()
   a = img
   b = a
   c = b
   d = c
   a = cv2.cvtColor(img, cv2.COLOR_HLS2BGR_FULL)
   cv2.imshow("green", a)

   kernal = np.ones((5,5), np.uint8 )
   b = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
   # b = cv2.dilate(img, kernal, iterations=1)
   # b = cv2.erode(img, kernal, iterations=1)
   cv2.imshow("yellow", b)


   c = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
   # c = cv2.dilate(img, kernal, iterations=1)
   # c = cv2.erode(img, kernal, iterations=1)
   cv2.imshow("green", c)


   d = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
   # d = cv2.dilate(img, kernal, iterations=1)
   # d = cv2.erode(img, kernal, iterations=1)
   cv2.imshow("red", d)
   if cv2.waitKey(1) and 0xFF == ord("q"):
        break
