import cv2
import numpy as np
from matplotlib import pyplot as plt
img_original = cv2.imread("img/simpson.jpg")
img_template = cv2.imread("img/marge.png")

#Apply template matching
res = cv2.matchTemplate(img_original,img_template,0)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(img_template.shape) #píxeles verticales y horizontales

print("imagen encontrada en "+str(min_loc))
w, h = min_loc

#Definimos los parámetros que necesita la función putText()
texto = "Marge"
posicion = (w-40,h)
fuente = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,255)
# cv2.line(img_original,(w,h),(w+10,h+150),(255,100,255),100)

cv2.putText(img_original,texto,posicion,fuente,1,color,2)
x,y = min_loc
cv2.rectangle(img_original, (min_loc), ( x+50,y+150), (0,0,0), 10)

plt.imshow(img_original)
plt.show()
