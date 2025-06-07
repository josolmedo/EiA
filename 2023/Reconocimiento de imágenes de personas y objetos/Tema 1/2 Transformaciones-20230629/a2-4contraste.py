import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread("manzana.png")
original = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

contraste = 240
nueva = imagenRGB.copy()
rows = imagenRGB.shape[0]
cols = imagenRGB.shape[1]

for ren in range(rows):
    for col in range(cols):
        for icolor in range(3):
          pixel = imagenRGB[ren][col][icolor] / contraste * 255
          nueva[ren,col,icolor] = pixel

figura = plt.figure(figsize=(10, 7))
figura.add_subplot(1, 2, 1)

plt.imshow(original)
plt.axis('off')
plt.title("Original")

figura.add_subplot(1, 2, 2)

plt.imshow(nueva)
plt.axis('off')
plt.title("Cambio de contraste")