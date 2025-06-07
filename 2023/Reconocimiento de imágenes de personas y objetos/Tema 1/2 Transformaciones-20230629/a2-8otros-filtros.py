import cv2
import numpy as np
import matplotlib.pylab as plt

#imagenBGR = cv2.imread('ruido1.png')
imagenBGR = cv2.imread('ruido2.png')
#imagenBGR = cv2.imread('ruidoCasa.jpg')
#imagenBGR = cv2.imread('filtrado.png')

imagenRGB = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2RGB)

filtro = 1

if filtro == 1:
  resultado = cv2.medianBlur(imagenRGB,5)
  titulo = "Con filtro de la mediana 5x5"
elif filtro == 2:
  resultado = cv2.GaussianBlur(imagenRGB,(5,5),0)
  titulo = "Con filtro gausiano 5x5"
elif filtro == 3:
  resultado = cv2.blur(imagenRGB,(3,3))
  titulo = "Con difuminación"

# DESPLIEGA IMAGENES
figura = plt.figure(figsize=(10, 7))
figura.add_subplot(1, 2, 1)
plt.imshow(imagenRGB)
plt.axis('off')
plt.title("Original con ruido")

figura.add_subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis('off')
plt.title(titulo)

# GUARDA EL RESULTADO
cv2.imwrite("filtrado"+str(filtro)+".png", resultado)
