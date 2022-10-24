import numpy as np
import matplotlib.pyplot as plt
import cv2

img_bruitee = cv2.imread("butterfly_noise_local.png")

'''crée une nouvelle image, dans laquelle chaque pixel est égal à la moyenne de ses voisins de l'image originale. 
Vous considérerez un voisinage de taille 1, c'est-à-dire pour un pixel (i, j) tous les pixels de i-1 à i+1 et de j-1 à j+1.'''
def moyenne_voisins(img):
    new_img = np.zeros(img.shape, dtype = 'int16')
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            # pas besoin de boucle sur les caneaux car image en niveaux de gris
                temp = 0
                num = 0
                #utiliser np.mean a la place pour les deux boucles
                for l in range (-1, 2):
                    for t in range (-1,2):
                        temp += img[i+l, j+t, 0]
                        num += 1
                new_img[i,j,0] = temp/num
                new_img[i,j,1] = temp/num
                new_img[i,j,2] = temp/num
    return new_img

  '''la taille du voisinage est donnée par `half_size`'''
  def moyenne_voisins_hs(img, half_size):
    new_img = np.zeros(img.shape, dtype = 'int16')
    for i in range(half_size, img.shape[0]-half_size):
        for j in range(half_size, img.shape[1]-half_size):
            # pas besoin de boucle sur les caneaux car image en niveaux de gris
                temp = 0
                num = 0
                #utiliser np.mean a la place pour les deux boucles
                for l in range (-half_size, half_size+1):
                    for t in range (-half_size, half_size+1):
                        temp += img[i+l, j+t, 0]
                        num += 1
                new_img[i,j,0] = temp/num
                new_img[i,j,1] = temp/num
                new_img[i,j,2] = temp/num
    return new_img

'''`noyau` est une matrice carrée, de taille `half_size`\*2+1, dont les valeurs sont binaires (0 ou 1). 
Pour chaque pixel (i, j) de `img`, considérez `noyau` comme étant centré en (i, j). 
Pour chaque pixel du voisinage, une valeur de `noyau` de 1 indique que le pixel à cette position doit être pris en compte dans le calcul, et une valeur de 0 indique qu'il doit être ignoré.'''
def moyenne_voisins_convolution(img, noyau):
    half_size = int((noyau.shape[0]-1)/2)
    new_img = np.zeros(img.shape, dtype = 'int16')
    for i in range(half_size, img.shape[0]-half_size):
        for j in range(half_size, img.shape[1]-half_size):
            temp = 0
            num = 0
            kl = 0
            for l in range (-half_size, half_size+1):
                    kt = 0
                    for t in range (-half_size, half_size+1):
                        if noyau[kl,kt]==1:
                            temp += img[i+l, j+t, 0]
                            num += 1
                        kt+=1
                    kl+=1
            new_img[i,j,0] = temp/num
            new_img[i,j,1] = temp/num
            new_img[i,j,2] = temp/num

    return new_img
  
img_debruitee = moyenne_voisins(img_bruitee)
  
half_size = 3
img_debruitee_hs = moyenne_voisins_hs(img_bruitee, half_size)

half_sizec = 8
size = half_sizec * 2 + 1
noyau = np.ones((size, size))
img_debruitee_conv = moyenne_voisins_convolution(img_bruitee, noyau)
