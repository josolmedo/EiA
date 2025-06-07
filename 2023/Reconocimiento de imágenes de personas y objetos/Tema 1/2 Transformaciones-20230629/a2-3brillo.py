import cv2
import matplotlib.pyplot as plt

archivo = "persona.jpg"
imagen = cv2.imread(archivo)
original = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

brillo = 80

nueva = imagenRGB.copy()
renglones = imagenRGB.shape[0]
columnas = imagenRGB.shape[1]

for ren in range(renglones):
    for col in range(columnas):
        for icolor in range(3):
          pixel = imagenRGB[ren][col][icolor] + brillo
          if pixel > 255:
            nueva[ren,col,icolor] = 255
          elif pixel < 0:
            nueva[ren,col,icolor] = 0
          else:
            nueva[ren,col,icolor] = pixel

figura = plt.figure(figsize=(10, 7))
figura.add_subplot(1, 2, 1) #RENGLONES, COLUMNAS, NÚMERO
plt.imshow(original)
plt.axis('off')
plt.title("Original")

figura.add_subplot(1, 2, 2) #RENGLONES, COLUMNAS, NÚMERO
plt.imshow(nueva)
plt.axis('off')
plt.title("Cambio de brillo")

cv2.imwrite("brillo-"+archivo, nueva)