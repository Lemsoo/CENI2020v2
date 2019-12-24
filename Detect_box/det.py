import cv2
import numpy as np7

def match(matchvalue):
    img2 = img.copy()

    result = cv2.matchTemplate(img,template,matchvalue)

    cv2.normalize(result,result,0,255,cv2.NORM_MINMAX)

    mini,maxi,(mx,my),(Mx,My) = cv2.minMaxLoc(result)    # We find minimum and maximum value locations in result

    if matchvalue in [0,1]: # For SQDIFF and SQDIFF_NORMED, the best matches are lower values.
        MPx,MPy = mx,my
    else:                   # Other cases, best matches are higher values.
        MPx,MPy = Mx,My

    # Normed methods give better results, ie matchvalue = [1,3,5], others sometimes shows errors
    cv2.rectangle(img2, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    cv2.imshow('input',img2)
    cv2.imshow('output',result)

img = cv2.imread('41.jpg')
template = cv2.imread('template.jpg')

trows,tcols = template.shape[:2]    # template rows and cols

cv2.namedWindow('input')

matchvalue = 0
max_Trackbar = 5

cv2.createTrackbar('method','input',matchvalue,max_Trackbar,match)

match(0)

if cv2.waitKey(0) == 27:
	cv2.destroyAllWindows()
