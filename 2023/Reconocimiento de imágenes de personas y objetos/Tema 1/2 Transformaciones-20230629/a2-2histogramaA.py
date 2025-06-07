import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread("mezcla.png")
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

color = ('b','g','w')
for i,col in enumerate(color):
  histograma = cv2.calcHist([imagenRGB],[i],None,[256],[0,256])
  plt.plot(histograma ,color = col)
  #plt.xlim([0,256])
  plt.xlim([10,250])
  plt.ylim([0,3000])
plt.show()
