import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow # DESPLIEGUE DE IMAGENES
from skimage import io
from PIL import Image
import matplotlib.pylab as plt

imagen = io.imread('clima1.png')
imagenRGB = cv.cvtColor(imagen, cv.COLOR_BGR2RGB)
print('Imagen original\nAncho: ',imagenRGB.shape[1])
print('Altura: ',imagenRGB.shape[0])
print('Canales: ',imagenRGB.shape[2])
print('\n')

gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
plt.hist(gris.ravel(),bins = 256, range = [0, 256])
plt.show()

#ret, binaria = cv.threshold(gris, 200, 255, cv.THRESH_BINARY)
ret, binaria = cv.threshold(gris, 150, 200, cv.THRESH_BINARY)

# DESPLIEGUE DE AMBAS IMAGENES
figura = plt.figure(figsize=(14, 8))
figura.add_subplot(1, 2, 1)
plt.imshow(imagenRGB)
plt.axis('off')
plt.title("Original")

figura.add_subplot(1, 2, 2)
resultado = cv2.merge((binaria, binaria, binaria))
plt.imshow(resultado)
plt.axis('off')
plt.title("Segmentación por tono de gris")
