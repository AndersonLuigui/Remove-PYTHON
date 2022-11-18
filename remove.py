from rembg import remove
from PIL import Image

#IMPORTANDO IMAGEM
img = Image.open('img.png')

#REMOVE FUNDO DE IMAGEM
img_without_back = remove(img)

#SALVA IMAGEM SEM FUNDO
img_without_back.save('img_without_back.png')