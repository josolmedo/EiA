import cv2
import numpy as np
import matplotlib.pylab as plt

original = cv2.imread('clima1.png')
grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
#imagen = cv2.bitwise_not(original, original) # FONDO DEBE SER BLANCO

kernel = np.ones((3, 3), np.uint8)

# DESPLIEGUE DE AMBAS IMAGENES
figura = plt.figure(figsize=(14, 8))
primera = cv2.merge((grises,grises,grises))
figura.add_subplot(1, 2, 1)
plt.imshow(primera)
plt.axis('off')
plt.title("Original")

ret, binaria = cv2.threshold(grises, 200, 255, cv2.THRESH_BINARY)


operacion = 3 #1=erosión, 2=dilatación, 3=cerradura, 4=apertura
if operacion == 1:
  resultado = cv2.erode(binaria, kernel, iterations=1)
  titulo = "Imagen erosionada"
elif operacion == 2:
  resultado = cv2.dilate(binaria, kernel, iterations=2)
  titulo ="Imagen dilatada"
elif operacion == 3:
  resultado = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel)
  titulo = "Imagen con cerradura"
elif operacion == 4:
  resultado = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
  titulo = "Imagen con apertura"

figura.add_subplot(1, 2, 2)
sale = cv2.merge((resultado,resultado,resultado))
plt.imshow(sale)
plt.axis('off')
plt.title(titulo)