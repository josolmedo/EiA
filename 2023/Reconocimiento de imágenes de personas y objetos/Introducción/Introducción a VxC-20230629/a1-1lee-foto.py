import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread("manzana.png")
imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.title("Manzana RGB")
plt.imshow(imagenRGB)
