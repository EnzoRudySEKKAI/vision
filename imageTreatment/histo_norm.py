import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("butterfly_gray.png")
val_min = 100
val_max = 125

'''calcule l'histogramme d'intensité d'une image en niveaux de gris. 
L'histogramme d'intensité d'une image peut être vu comme un tableau à une dimension dont chaque case contient le nombre de pixels à une certaine valeur d'intensité.'''
def histogram(img):
    example = np.zeros((256))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                example[img[i,j,k]]+= 1
    return example
  
'''Cette fonction a pour effet de réduire ou d'augmenter le contraste, respectivement en comprimant ou en étirant les valeurs d'intensité de l'image d'entrée vers les valeurs val_min et val_max.'''  
def normalize(img, val_min, val_max):
    img_max = np.max(img)
    img_min = np.min(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                temp = (img[i,j,k] - img_min)/(img_max - img_min)
                img[i, j, k] = temp*(val_max-val_min)+val_min
                
img_normalized = normalize(img, val_min, val_max)
hist = histogram(img)

histn = histogram(img_normalized)
if histn is not None:
    plt.bar(np.arange(len(histn)), histn)
