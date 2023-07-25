from PIL import Image
import numpy as np

def imagens_sao_iguais(imagem1, imagem2):
    # Carregar as duas imagens usando a PIL
    img1 = Image.open(imagem1)
    img2 = Image.open(imagem2)

    # Converter as imagens para arrays numpy
    array1 = np.array(img1)
    array2 = np.array(img2)

    # Comparar os arrays numpy pixel a pixel
    if np.array_equal(array1, array2):
        return True
    else:
        return False

# Exemplo de uso
imagem_original = "imagem_original.png"
imagem_copiada = "X.png"

if imagens_sao_iguais(imagem_original, imagem_copiada):
    print("As imagens são iguais.")
else:
    print("As imagens são diferentes.")