import cv2
import numpy as np
import pytesseract

#Faire les commandes suivantes pour installer pytesseract

#"pip3 install pytesseract" pour python 3 et pip au lieu de pip3 pour python2

#sudo apt update
#sudo apt install tesseract-ocr
#sudo apt install libtesseract-dev

f=open("listeNum.txt","a+")
def detect_case(img):
    img2 = cv2.imread(img)     

    n=0 
    for i in range(65,95):
        for j in range(35,65):
            if img2[i, j][0] >= 200 and img2[i, j][1] >= 200 and img2[i, j][2] >= 200  :
                n=n+1
                

   #Les numeros 65,95,35,65 sont les coordonnées des 4 pixels sommets du rectangle qui doit etre vide pour les personnes qui n'ont pas voté 

    if n>850:
        print("Il n'a pas voté et son Numero a été ajouté au fichier texte listeNum.txt")
        f.write(pytesseract.image_to_string(img2)[0:11]+"--------------------------" +"\n")        


        return 0
        
    else :
        print("Il a pas voté")
        return 1

detect_case("2.png")
