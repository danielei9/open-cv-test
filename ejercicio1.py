import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#Cargamos una imagen
img = cv2.imread("img/xiquet.jpg")

#Mostramos una imagen
#cv2.imshow("My Image",img) #el primer parámetro es el nombre de la ventana, que puedo poner el que quiera
cv2.waitKey(0) #aprieta una tecla 
cv2.destroyAllWindows()

#Escribimos en una imagen
cv2.imwrite("image_copy.jpg",img)

#Propiedades de la imagen
print(type(img))
print(img.shape) #píxeles verticales y horizontales
print(img.size)
print(img.dtype)

top_left_px = img[0,0,:] #esto me devuelve una lista de 3 valores (BGR) del pixel 0,0
print(top_left_px)

top_left_px_R = img[0,0,2] #esto me devuelve solo la componente R
print(top_left_px_R)


R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
print("R': ",R,"\nG': ", G,"\nB': ", B)
imgGray =  R*0.299 + G* 0.587 + B*0.114 #mediante la fórmula NTSC: 0.299 ∙ Rojo + 0.587 ∙ Verde + 0.114 ∙ Azul. Esta fórmula representa la percepción relativa de la persona promedio del brillo de la luz roja, verde y azul.

print("R': ",R,"\nG': ", G,"\nB': ", B)
plt.imshow(imgGray, cmap='gray')
plt.show()

cv2.imwrite('imgGray.png', imgGray)