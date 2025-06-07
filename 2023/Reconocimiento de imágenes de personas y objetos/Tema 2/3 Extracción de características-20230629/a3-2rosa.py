import cv2
import numpy as np
 
imagenBGR = cv2.imread('rosa.png')
imagenRGB = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2RGB)
imagenHSV = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2HSV)
 
# SELECCIÓN DEL ROJO EN EL RANGO H:(0 - 10)
inferior1 = np.array([0, 100, 20])
superior1 = np.array([10, 255, 255])
 
# SELECCIÓN DEL ROJO EN EL RANGO H:(160 - 180)
inferior2 = np.array([160,100,20])
superior2 = np.array([179,255,255])

# MASCARAS DE SELECCIÓN 
mascara1 = cv2.inRange(imagenHSV, inferior1, superior1)
mascara2 = cv2.inRange(imagenHSV, inferior2, superior2)
 
mascara = mascara1 + mascara2
 
seleccion = cv2.bitwise_and(imagenRGB, imagenRGB, mask=mascara)
 
figura = plt.figure(figsize=(15, 7))
figura.add_subplot(1, 3, 1)
plt.imshow(imagenRGB)
plt.axis('off')
plt.title("Rosa original")

figura.add_subplot(1, 3, 2)
mostrar = cv2.merge((mascara,mascara,mascara))
plt.imshow(mostrar)
plt.axis('off')
plt.title("Máscara")

figura.add_subplot(1, 3, 3)
plt.imshow(seleccion)
plt.axis('off')
plt.title("Selección en RGB")