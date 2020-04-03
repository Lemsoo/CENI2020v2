import os, re, sys, cv2, shutil, json
import numpy as np
import pytesseract as pyt
from pdf2image import convert_from_path, convert_from_bytes


#va generer une fichier de type json 

idx = 0
numError = 0
index = 0
tcid = {}
class CENI:
    global idx
    global numError
    global tcid

    #for converting pdf to img
    def convertTopdf(self, *pdf):

        images = convert_from_path(*pdf)
        i = 1
        for image in images:
        	image.save('./src_img/' + str(i) + '.jpg', 'JPEG')
        	i = i + 1


    def detect_case(self, img):
        img = img.split(" ")
        global numError
        global index
        global tcid
        for image in img:
            img2 = cv2.imread(image)
            if img2.shape[1] < 1400:
                n=0
                try :
                    for i in range(60,150):
                        for j in range(20,120):
                            if img2[i, j][0] == 255 and img2[i, j][1] == 255 and img2[i, j][2] == 255 :
                                n=n+1
                except IndexError as e:
                    numError+=1
                    #print(e)
                    cv2.imwrite('error.png',img2)
                    pass

               #Les numeros 60,150,20,120 sont les coordonnées des 4 pixels sommets du rectangle qui doit etre vide pour les personnes qui n'ont pas voté

                if n>8000:
                    index += 1
                    #g = pyt.image_to_string(img2).split("\n")
                    g = pyt.image_to_string(img2)
                    f_ = self.getText(g)
                    tcid['p' + str(index)] = f_
                    #f.write(str(f_) + "\n")
                    #cv2.imwrite('./vot/' + str(index) + '.png',img2)


    def getText(self, g):
        f={}
        for j in g.split("\n"):
            nni = re.search( r'[0-9]{10,11}', j, re.M|re.I)
            f_name = re.search( r'[A-Za-z\']{3,30}\s[A-Za-z\']{3,30}\s[A-Za-z\']{3,30}', j, re.M|re.I)#[\sA-Za-z\']{0,30}', j, re.M|re.I)
            date_of_birth = re.search( r'[\d]{2}/[\d]{2}/[\d]{4}', j, re.M|re.I)
            sexe = re.search( r'\b(M|F|E)\b', j, re.M)

            if nni :
                f['NNI'] = nni.group()
            if f_name:
                f['name'] = f_name.group()
                if len(f['name']) < len(f_name.group()) :
                    f['name'] = f_name.group()
            if date_of_birth :
                f['date_of_birth'] = date_of_birth.group()
            if sexe:
                Sexe = sexe.group()
                f['sexe'] = Sexe
                if Sexe == 'E':
                    f['sexe'] = Sexe
                    Sexe = 'F'

        return f

    # une fonction pour trier les jpg decouper
    def sort_contours(self, cnts, method="left-to-right"):
        # initialize the reverse flag and sort index
        reverse = False
        i = 0

        # handle if we need to sort in reverse
        if method == "right-to-left" or method == "bottom-to-top":
            reverse = True

        # handle if we are sorting against the y-coordinate rather than
        # the x-coordinate of the bounding box
        if method == "top-to-bottom" or method == "bottom-to-top":
            i = 1

        # construct the list of bounding boxes and sort them from top to
        # bottom
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][i], reverse=reverse))

        # return the list of sorted contours and bounding boxes
        return (cnts, boundingBoxes)



    def box_extraction(self, param, *img_for_box_extraction_path):
        global idx
        img_for_box_extraction_path = list(img_for_box_extraction_path)
        for image in img_for_box_extraction_path:
            img = cv2.imread(image, 0)  # Read the image
            (thresh, img_bin) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Thresholding the image

            img_bin = 255-img_bin  # Invert the image


            # Defining a kernel length
            kernel_length = np.array(img).shape[1]//40

            # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
            verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
            # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
            hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
            # A kernel of (3 X 3) ones.
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

            # Morphological operation to detect verticle lines from an image
            img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=2)
            verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3) #7

            # Morphological operation to detect horizontal lines from an image
            img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=2)
            horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=8)

            # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
            alpha = 0.5
            beta = 1.0 - alpha
            # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
            img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
            img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
            (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            # Find contours for image, which will detect all the boxes
            contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # Sort all the contours by top to bottom.
            (contours, boundingBoxes) = self.sort_contours(contours, method="top-to-bottom")

            for c in contours:
                # Returns the location and width,height for every contour
                x, y, w, h = cv2.boundingRect(c)

                # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
                if (w > 80 and h > 20) and w > 3*h:

                    idx += 1
                    new_img = img[y:y+h, x:x+w]
                    #images.append(new_img)
                    cv2.imwrite(param + str(idx) + '.png', new_img)

        #return images
            # For Debugging
            # Enable this line to see all contours.
            # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
            # cv2.imwrite("./Temp/img_contour"+str(idx2)+".jpg", img)



os.mkdir("src_img")
os.mkdir("Cropped")

A = CENI()
f=open("person_non_voter.json","w+")
a=os.listdir("src_img")
A.convertTopdf(str(sys.argv[1]))

for file in os.listdir("./src_img/"):
    if file.endswith(".jpg"):
        A.box_extraction("./Cropped/", "./src_img/" + str(file))

b="Cropped/"
b_=os.listdir("./Cropped/")
b = b + " Cropped/".join(b_)
A.detect_case( b)
json.dump(tcid, f)
print (numError)
f.close()
shutil.rmtree("src_img")
shutil.rmtree("Cropped")
