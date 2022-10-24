import numpy as np
import matplotlib.pyplot as plt
import cv2
img = cv2.imread("butterfly_gray.png")

'''Cette fonction renvoie une nouvelle image dans laquelle chaque pixel (x,y) équivaut à la valeur la plus **faible** parmi les pixels voisins. 
Le voisinage considéré pourra être un carré allant de (x-half_size, y-half_size) à (x+half_size, y+half_size), 
c'est-à-dire un carré centré en (x-y) de taille size=(2\*half_size)+1.
On considèrera que les 3 canaux sont identiques (image en niveau de gris sur 3 canaux).'''
def erosion(img, half_size=2):
    new_img = np.zeros(img.shape, dtype = 'int16')

    for i in range(half_size, img.shape[0]-half_size):
        for j in range(half_size, img.shape[1]-half_size):
            minr = img[i, j,0]
            for l in range (-half_size, half_size+1):
                    for t in range (-half_size, half_size+1):
                        if img[i+l, j+t,0] < minr:
                            minr = img[i+l, j+t,0]
            new_img[i, j,0] = minr
            new_img[i, j,1] = minr
            new_img[i, j,2] = minr
    return new_img

'''Cette fonction, à l'instar de la fonction erosion, renvoie une nouvelle image dans laquelle chaque pixel (x,y) équivaut à la valeur la plus **élevée** parmi les pixels voisins.
On considèrera à nouveau que les 3 canaux sont identiques (image en niveau de gris sur 3 canaux).'''
def dilation(img, half_size=2):
    new_img = np.zeros(img.shape, dtype = 'int16')

    for i in range(half_size, img.shape[0]-half_size):
        for j in range(half_size, img.shape[1]-half_size):
            minr = img[i, j,0]
            for l in range (-half_size, half_size+1):
                    for t in range (-half_size, half_size+1):
                        if img[i+l, j+t,0] > minr:
                            minr = img[i+l, j+t,0]
            new_img[i, j,0] = minr
            new_img[i, j,1] = minr
            new_img[i, j,2] = minr
    return new_img

img_dilatee = dilation(img, 2)
img_erodee = erosion(img, 2)

def getEdgesV1():
    contours = img_dilatee - img_erodee
    plt.imshow(contours)

'''(more precise)'''
def getEdgesV2():
    contours = img.astype(np.int16)
    contours *= 2
    contours -= img_dilatee
    contours -= img_erodee
    plt.imshow(np.clip(contours, a_min=0, a_max=255))

'''(too precise)'''
def getEdgesV3():
    contours = img.astype(np.int16)
    contours *= 2
    contours -= erosion(dilation(img))
    contours -= dilation(erosion(img))
    plt.imshow(np.clip(contours, a_min=0, a_max=255))

