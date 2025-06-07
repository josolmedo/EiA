import cv2
import numpy as np
import matplotlib.pyplot as plt

archivo = "ruido2.png"
original = cv2.imread(archivo)

kernel = np.ones((5,5),np.float32)/ (5*5)
#kernel = np.ones((3,3),np.float32)/ (3*3)
#kernel = np.array([[-2,-1,0],[-1, 1, 1],[0, 1, 2]]) # REPUJADO 
#kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]]) # ENFOQUE
#kernel = np.array([[-2,-1,0],[-1, 1, 1],[0, 1, 2]]) # REPUJADO
#kernel = np.array([[-1,-1,-1],[-1, 8, -1],[-1, -1, -1]]) # DETECCION DE BORDES 1 mejor
#kernel = np.array([[1/9, 1/9, 1/9],[1/9, 1/9, 1/9],[1/9, 1/9, 1/9]]) # DESENFOQUE

filtrada = cv2.filter2D(original, -1, kernel) # APLICANDO EL KERNEL

figura = plt.figure(figsize=(10, 7))
figura.add_subplot(1, 2, 1)
plt.imshow(original)
plt.axis('off')
plt.title("Original con ruido")

figura.add_subplot(1, 2, 2)
plt.imshow(filtrada)
plt.axis('off')
plt.title("Con filtro de la media 3x3")

# GUARDA EL RESULTADO
cv2.imwrite("filtro-"+archivo, nueva)