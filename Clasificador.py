import numpy as np 
import cv2
imagen = cv2.imread('imagen.jpg')
m,n,c=imagen.shape
imagenb=np.zeros((m,n))

for x in range(m):
    for y in range(n):
        if(0<imagen[x,y,0]<241) and (0<imagen[x,y,1]<255) and (0<imagen[x,y,2]<255):
            imagenb[x,y]=255
cv2.imshow('imagenb',imagenb)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Resultado.jpg',imagenb)
