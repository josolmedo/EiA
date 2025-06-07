import cv2

archivos = ["rect1.png","rect2.png","rect3.png","rect4.png"] 
for i in range(0,len(archivos)):
  archivo = archivos[i]
  imagenGrises = cv2.imread(archivo, cv2.IMREAD_GRAYSCALE)
  res,imagenBN = cv2.threshold(imagenGrises, 128, 255, cv2.THRESH_BINARY)

  # CALCULA LOS MOMENTOS
  momentos = cv2.moments(imagenBN)
  # CALCULA LOS MOMENTOS DE HU
  momentosHU = cv2.HuMoments(momentos)

  # DESPLEGAR MOMENTOS POR ARCHIVO
  print("{}: ".format(archivo),end='')
  print(momentos)
  print()

  print("{}: ".format(archivo),end='')
  for i in range(0,7):
      # Hu Moments without log transform
      print(i,momentosHU[i],end=' ')
  print()

  xCentroide = momentos["m10"] / momentos["m00"] 
  yCentroide = momentos["m01"] / momentos["m00"] 
  print("***CENTROIDE:",int(xCentroide), int(yCentroide))
  
  area = momentos["m00"]
  print("***ÁREA:",int(area))
