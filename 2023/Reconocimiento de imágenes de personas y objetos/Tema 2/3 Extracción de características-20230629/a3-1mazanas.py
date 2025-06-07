# DETECTA MANZANAS ROJAS
import cv2
import matplotlib.pyplot as plt

#imagen = cv2.imread("mezcla.png")
#imagen = cv2.imread("manzana.png")
imagen = cv2.imread("manzana2.png")

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

color = ('c','y','k')
for i,col in enumerate(color):
  histograma = cv2.calcHist([imagenHSV],[i],None,[256],[0,256])
  plt.plot(histograma ,color = col)
  plt.xlim([0,256])
  #plt.xlim([10,250])
  #plt.ylim([0,3000])
plt.show()

print("HSV ", imagenHSV.shape)
h,s,v = cv2.split(imagenHSV)
print(v.size)
for ren in range(imagenHSV.shape[0]):
  for col in range(imagenHSV.shape[1]):
    if v[ren][col] < 70: # and s[ren][col] > 220:
      v[ren][col] = 0
      s[ren][col] = 0
      h[ren][col] = 0
    else:  
      v[ren][col] = 200
    if (h[ren][col] > 0 and h[ren][col] < 20 and s[ren][col] > 150) or (h[ren][col] > 175 and s[ren][col] > 150):
      h[ren][col] = 90
      s[ren][col] = 255
      v[ren][col] = 255

reintegrada = cv2.merge((h,s,v))
nueva= cv2.cvtColor(reintegrada, cv2.COLOR_HSV2RGB)
plt.imshow(nueva)

plt.axis('off')
plt.title("Selección")
