'''les 3 canaux sont traités conjointement. Pour 2 pixels considérés, le triplet (r,g,b) considéré comme "supérieur" est celui :
- Du pixel qui a une valeur de rouge supérieure, s'il y en a un.
- Sinon, celui du pixel qui a une valeur de vert supérieure, s'il y en a un.
- Sinon, celui du pixel qui a une valeur de bleu supérieure, s'il y en a un.
- Sinon, les deux pixels sont égaux (on peut garder n'importe lequel des deux).

Pour l'érosion, on cherchera donc le triplet (r, g, b) *inférieur*.

Pour la dilation, on cherchera donc le triplet (r, g, b) *supérieur*.'''

def erosion_lexico(img, half_size=2):
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
                            minv = img[i+l, j+t,1]
                            minb = img[i+l, j+t,2]
                        elif img[i+l, j+t,1] < minv and img[i+l, j+t,0] == minr:
                            minr = img[i+l, j+t,0]
                            minv = img[i+l, j+t,1]
                            minb = img[i+l, j+t,2]
                        elif img[i+l, j+t,2] < minb and img[i+l, j+t,0] == minr and img[i+l, j+t,1] == minv:
                            minr = img[i+l, j+t,0]
                            minv = img[i+l, j+t,1]
                            minb = img[i+l, j+t,2]
                        
            new_img[i, j,0] = minr
            new_img[i, j,1] = minv
            new_img[i, j,2] = minb
    return new_img

def dilation_lexico(img, half_size=2):
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
                            minv = img[i+l, j+t,1]
                            minb = img[i+l, j+t,2]
                        elif img[i+l, j+t,1] > minv and img[i+l, j+t,0] == minr:
                            minr = img[i+l, j+t,0]
                            minv = img[i+l, j+t,1]
                            minb = img[i+l, j+t,2]
                        elif img[i+l, j+t,2] > minb and img[i+l, j+t,0] == minr and img[i+l, j+t,1] == minv:
                            minr = img[i+l, j+t,0]
                            minv = img[i+l, j+t,1]
                            minb = img[i+l, j+t,2]
                        
            new_img[i, j,0] = minr
            new_img[i, j,1] = minv
            new_img[i, j,2] = minb
    return new_img

img_dilatee = dilation_lexico(carre_magique, 2)
img_erodee = erosion_lexico(carre_magique, 2)
