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

# [80,110] NUBES FRIAS, [180,255] NUBES LLUVIA, [0, 60] ALTA PRESIÓN
inferior = 80
superior = 110
seleccion = imagenRGB.copy()

renglones = imagenRGB.shape[0]
columnas = imagenRGB.shape[1]

for ren in range(renglones):
    for col in range(columnas):
        if imagenGrises[ren][col] >= inferior and imagenGrises[ren][col] <= superior: 
          seleccion[ren][col] = (255,255,255)
        else:
          seleccion[ren][col] = (0,0,0)

figura = plt.figure(figsize=(10, 7))
figura.add_subplot(1, 2, 1) #RENGLONES, COLUMNAS, NÚMERO
plt.imshow(imagenRGB)
plt.axis('off')
plt.title("Original")

figura.add_subplot(1, 2, 2) #RENGLONES, COLUMNAS, NÚMERO
plt.imshow(seleccion)
plt.axis('off')
plt.title("Nubes frias")