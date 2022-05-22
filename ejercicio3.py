import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("img/xiquet.jpg")
imgGray = cv2.imread("imgGray.png")
imgRotate =cv2.imread("imgRotate.png")
#Comparamos cada imagen con la original mediate subtract: sustrae cada píxel y valor de color
diff_12 = cv2.subtract(img,imgGray)
print(np.sum(diff_12)/np.sum(img)*100,'%' )

#redimensionamos para poder comparar con la girada
imgRotate = cv2.resize(imgRotate, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
img = cv2.resize(img, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
imgGray = cv2.resize(imgGray, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)

diff_12 = cv2.subtract(img,imgRotate)
print(np.sum(diff_12)/np.sum(img)*100,'%' )
diff_12 = cv2.subtract(imgGray,imgRotate)
print(np.sum(diff_12)/np.sum(imgGray)*100,'%' )
print()

#Sumamos todos los elementos del array diferencia para obtener un número representativo de cómo de similares o diferentes son
