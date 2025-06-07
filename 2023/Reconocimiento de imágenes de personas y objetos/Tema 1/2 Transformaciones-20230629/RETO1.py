import cv2
import numpy as np

#ROJO
imagenBGR = np.uint8([[[0,0,255]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("rojo\t\t",imagenHSV)

#AMARILLO
imagenBGR = np.uint8([[[0,255,255]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("amarillo\t",imagenHSV)

#VERDE
imagenBGR = np.uint8([[[0,255,0]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("verde\t\t",imagenHSV)

#AZUL CIELO
imagenBGR = np.uint8([[[255,255,0]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("azul cielo\t",imagenHSV)

#AZUL
imagenBGR = np.uint8([[[255,0,0]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("azul\t\t",imagenHSV)

#MAGENTA
imagenBGR = np.uint8([[[255,0,255]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("verde\t\t",imagenHSV)

#ROJO
imagenHSV = np.uint8([[[179,255,255]]])
imagenBGR = cv2.cvtColor(imagenHSV,cv2.COLOR_HSV2BGR)
print("\nrojo BGR\t",imagenBGR)

#ROJO
imagenBGR = np.uint8([[[5,0,255]]])
imagenHSV = cv2.cvtColor(imagenBGR,cv2.COLOR_BGR2HSV)
print("rojo HSV\t",imagenHSV)