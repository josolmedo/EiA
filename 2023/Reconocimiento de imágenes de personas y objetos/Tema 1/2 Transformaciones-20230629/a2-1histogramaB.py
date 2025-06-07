import cv2
import matplotlib.pyplot as plt
import numpy as np

imagen = cv2.imread("mezcla.png")
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB) # BGR -> RGB
renglones = imagenRGB.shape[0]
columnas = imagenRGB.shape[1]

x = np.arange(0, 256)
r = np.zeros(256)
g = np.zeros(256)
b = np.zeros(256)
for ren in range(renglones):
    for col in range(columnas):
        pixel = imagenRGB[ren][col] # (r,g,b)
        r[pixel[0]] += 1
        g[pixel[1]] += 1
        b[pixel[2]] += 1

#fig = plt.figure(figsize=(6, 6))
plt.plot(x, r, color="red")
plt.plot(x, g, color="green")
plt.plot(x, b, color="blue")
plt.axis('on')
plt.xlim(left=10)
plt.xlim(right=250)
plt.ylim(top=700)
plt.ylim(bottom=0)
plt.title("Histograma RGB")