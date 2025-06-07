import cv2
import matplotlib.pyplot as plt

archivo = "clima1.png"
imagenBGR = cv2.imread(archivo)
imagenRGB = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2RGB)
imagenGrises = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2GRAY)
#print(imagenGrises.shape)
if len(imagenGrises.shape) == 2: # IMAGEN TONO DE GRISES
  renglones = imagenRGB.shape[0]
  columnas = imagenRGB.shape[1]
  histograma = cv2.calcHist([imagenGrises],[0],None,[256],[0,256])
  plt.plot(histograma ,color = 'k')
  plt.xlim([0,256])
plt.show()

# [80,110] NUBES FRIAS, [180,255] NUBES LLUVIA
inferior = 180
superior = 255

mascara = cv2.inRange(imagenGrises, inferior, superior)

seleccion = cv2.bitwise_and(imagenRGB, imagenRGB, mask=mascara)

figura = plt.figure(figsize=(10, 7))
figura.add_subplot(1, 2, 1) #RENGLONES, COLUMNAS, NÚMERO
plt.imshow(imagenRGB)
plt.axis('off')
plt.title("Original")

figura.add_subplot(1, 2, 2) #RENGLONES, COLUMNAS, NÚMERO
plt.imshow(seleccion)
plt.axis('off')
plt.title("Nubes frias")