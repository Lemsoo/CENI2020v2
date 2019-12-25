import cv2
import numpy as np

def detect_case(img):
    img2 = cv2.imread(img)     

    n=0 
    for i in range(65,95):
        for j in range(35,65):
            if img2[i, j][0] >= 200 and img2[i, j][1] >= 200 and img2[i, j][2] >= 200  :
                n=n+1
                

   #Les numeros 65,95,35,65 sont les coordonnées des 4 pixels sommets du rectangle qui doit etre vide pour les personnes qui n'ont pas voté 

    if n>850:
        print("Il n'a pas voté")
        return 0
    else :
        print("Il a bien voté")
        return 1

detect_case("41.png")
