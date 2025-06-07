import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread("manzana.png")
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

color = ('b','g','r')
for i,col in enumerate(color):
  histograma = cv2.calcHist([imagenRGB],[i],None,[256],[0,256])
  plt.plot(histograma ,color = col)
  plt.xlim([0,256])
plt.show()
