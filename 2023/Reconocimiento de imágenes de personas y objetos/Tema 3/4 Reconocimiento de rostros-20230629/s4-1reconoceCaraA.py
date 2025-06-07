import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# USA UN CLASIFICADOR DE CARAS PREDEFINIDO
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

print("Para salir, pulsa la letra s")
# ITERA CAPTURANDO IMAGENES DE VIDEO
while True:
    ret, frame = cap.read() # CAPTURA CADA CUADRO DE IMAGEN 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # CONVIERTE A GRISES LAS IMAGENES

    faces = faceClassif.detectMultiScale(gray, 2, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break;
cap.release()
cv2.destroyAllWindows()