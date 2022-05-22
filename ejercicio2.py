import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("img/xiquet.jpg")

R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
print("R: ",R/3,"\nG: ", G/3,"\nB: ", B/3)

plt.show()
R = np.rot90(R, k = 1, axes =(0, 1))
G = np.rot90(G, k = 1, axes =(0, 1))
B = np.rot90(B, k = 1, axes =(0, 1))
imgNew =  R/3 + G/3 + B/3
plt.imshow(imgNew, cmap='gray')
plt.show()
cv2.imwrite('imgRotate.png', imgNew)
