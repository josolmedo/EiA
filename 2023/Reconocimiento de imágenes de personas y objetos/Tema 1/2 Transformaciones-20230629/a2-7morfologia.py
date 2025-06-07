import cv2
import numpy as np
import matplotlib.pylab as plt

original = cv2.imread('binaria.png')
imagen = original
#imagen = cv2.bitwise_not(original, original) # FONDO DEBE SER BLANCO

kernel = np.ones((3, 3), np.uint8)

# DESPLIEGUE DE AMBAS IMAGENES
figura = plt.figure(figsize=(14, 8))
primera = cv2.merge((imagen,imagen, imagen))
figura.add_subplot(1, 2, 1)
plt.imshow(imagen)
plt.axis('off')
plt.title("Original")

operacion = 2 #1=erosión, 2=dilatación, 3=cerradura, 4=apertura
if operacion == 1:
  resultado = cv2.erode(imagen, kernel, iterations=1)
  titulo = "Imagen erosionada"
elif operacion == 2:
  resultado = cv2.dilate(imagen, kernel, iterations=2)
  titulo ="Imagen dilatada"
elif operacion == 3:
  resultado = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
  titulo = "Imagen con cerradura"
elif operacion == 4:
  resultado = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)
  titulo = "Imagen con apertura"
figura.add_subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis('off')
plt.title(titulo)

