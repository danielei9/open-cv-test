import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("img/futbol_reduced.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# cv2.imshow('hsv',hsv)
cv2.waitKey(0) #aprieta una tecla 
cv2.destroyAllWindows()

dark_blue=np.uint8([[[255,0,0]]])
hsv_dark_blue = cv2.cvtColor(dark_blue,cv2.COLOR_BGR2HSV)
print(hsv_dark_blue)
#[[[120 255 255]]]  --> esto es el color en HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# cv2.imshow('mask',mask)
cv2.waitKey(0) #aprieta una tecla 
cv2.destroyAllWindows()
res = cv2.bitwise_and(img, img, mask= mask)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(mask)
x,y = max_loc

cv2.rectangle(img, (x-100,y-100), ( x+100,y+100), (0,0,0), 10)


# cv2.imshow('res',res)
cv2.waitKey(0) #aprieta una tecla 
cv2.imshow('res',img)
cv2.waitKey(0) #aprieta una tecla 
cv2.destroyAllWindows()