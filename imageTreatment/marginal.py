import numpy as np
import matplotlib.pyplot as plt
import cv2

carre_magique = cv2.imread("carre_magique.png")
carre_magique = cv2.cvtColor(carre_magique, cv2.COLOR_BGR2RGB)

'''similaires aux fonctions erosion et dilation codées précédemment, à la différence que les 3 canaux de couleur sont traités séparément.'''
def erosion_marginal(img, half_size=2):
    new_img = np.zeros(img.shape, dtype = 'int16')

    for i in range(half_size, img.shape[0]-half_size):
        for j in range(half_size, img.shape[1]-half_size):
            minr = img[i, j,0]
            minv = img[i, j,1]
            minb = img[i, j,2]
            for l in range (-half_size, half_size+1):
                    for t in range (-half_size, half_size+1):
                        if img[i+l, j+t,0] < minr:
                            minr = img[i+l, j+t,0]
                        if img[i+l, j+t,1] < minv:
                            minv = img[i+l, j+t,1]
                        if img[i+l, j+t,2] < minb:
                            minb = img[i+l, j+t,2]
            new_img[i, j,0] = minr
            new_img[i, j,1] = minv
            new_img[i, j,2] = minb
    return new_img
  
def dilation_marginal(img, half_size=2):
    new_img = np.zeros(img.shape, dtype = 'int16')

    for i in range(half_size, img.shape[0]-half_size):
        for j in range(half_size, img.shape[1]-half_size):
            minr = img[i, j,0]
            minv = img[i, j,1]
            minb = img[i, j,2]
            for l in range (-half_size, half_size+1):
                    for t in range (-half_size, half_size+1):
                        if img[i+l, j+t,0] > minr:
                            minr = img[i+l, j+t,0]
                        if img[i+l, j+t,1] > minv:
                            minv = img[i+l, j+t,1]
                        if img[i+l, j+t,2] > minb:
                            minb = img[i+l, j+t,2]
            new_img[i, j,0] = minr
            new_img[i, j,1] = minv
            new_img[i, j,2] = minb
    return new_img

img_dilatee = dilation_marginal(carre_magique, 2)
img_erodee = erosion_marginal(carre_magique, 2)
