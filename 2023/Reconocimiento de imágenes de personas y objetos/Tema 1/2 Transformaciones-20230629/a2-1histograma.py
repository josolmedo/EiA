import cv2
import matplotlib.pyplot as plt
import numpy as np

imagen = cv2.imread("manzana.png")
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB) # BGR -> RGB
renglones = imagenRGB.shape[0]
columnas = imagenRGB.shape[1]
contador = 0
x = np.arange(0, 256)
r = np.zeros(256)
g = np.zeros(256)
b = np.zeros(256)
for ren in range(renglones):
    for col in range(columnas):
        pixel = imagenRGB[ren][col]
        r[pixel[0]] += 1
        g[pixel[1]] += 1
        b[pixel[2]] += 1

#fig = plt.figure(figsize=(6, 6))
plt.plot(x, r, color="red")
plt.plot(x, g, color="green")
plt.plot(x, b, color="blue")
#plt.axis('off')
plt.title("Histograma RGB")
