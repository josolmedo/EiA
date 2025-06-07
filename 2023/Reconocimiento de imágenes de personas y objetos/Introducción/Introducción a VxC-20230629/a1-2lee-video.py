import imageio
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import cv2

def muestraVideo(video):
    figura = plt.figure(figsize=(3,3))
    mov = []
    for i in range(len(video)):
        imagen = video[i]

        # IMAGEN RGB
        img = plt.imshow(imagen, animated=True)

        # CONVERSION A GRISES DE UNA IMAGEN
        #gris = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        #grises = cv2.merge([gris,gris,gris])
        #img = plt.imshow(grises, animated=True)

        # SEPARACION DEL CANAL ROJO
        #r, g, b = cv2.split(imagen)
        #resultado = cv2.merge([r,r,r])
        #img = plt.imshow(resultado, animated=True)

        plt.axis('off')
        mov.append([img])
    anime = animation.ArtistAnimation(figura, mov, interval=50, repeat_delay=1000)
    plt.close()
    return anime

video =  imageio.mimread('prueba.mp4')
HTML(muestraVideo(video).to_html5_video())