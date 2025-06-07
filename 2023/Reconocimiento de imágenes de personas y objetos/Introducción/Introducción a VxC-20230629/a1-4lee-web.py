import cv2 as cv
from google.colab.patches import cv2_imshow # for image display
from skimage import io

# DIRECCIONES WEB DE EJEMPLO
urls = ["https://iiif.lib.ncsu.edu/iiif/0052574/full/800,/0/default.jpg",
       "https://iiif.lib.ncsu.edu/iiif/0016007/full/800,/0/default.jpg",
      "https://placekitten.com/800/571"]

# CARGA CADA IMAGEN
for url in urls:
  imagen = io.imread(url)
  imagenRGB = cv.cvtColor(imagen, cv.COLOR_BGR2RGB)
  imagenUnidas = cv.hconcat((imagen, imagenRGB))
  print('Ancho: ',imagenRGB.shape[1])
  print('Alto: ',imagenRGB.shape[0])
  print('Número canales: ',imagenRGB.shape[2])
  cv2_imshow(imagenUnidas)
  print('\n')