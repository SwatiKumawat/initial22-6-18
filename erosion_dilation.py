#!/usr/bin/python2

import cv2
import numpy as np
import pytesseract

img = cv2.imread("test.png")
'''
bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(bw,145,255,cv2.THRESH_BINARY)

#taking matrix of 5 as kernel
kernel = np.ones((5,5),np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img,kernel,iterations=1)

#cv2.imshow("orig",img)
cv2.imshow("erosion",img_erosion)
cv2.imshow("dilated",img_dilation)
'''
kernel = np.ones((3,3),np.uint8)

img_erosion1 = cv2.erode(img, kernel, iterations=1)
img_dilation1 = cv2.dilate(img_erosion1,kernel,iterations=1)

#cv2.imshow("orig",img)
cv2.imshow("erosion1",img_erosion1)
cv2.imshow("dilated1",img_dilation1)

cv2.waitKey(0)

config = ('-l eng --oem 1 --psm 3')

#converting image text to string
text = pytesseract.image_to_string(img_dilation1, config=config)
#printing the extracted text
print (text)
'''
print ('*' * 10)
text = pytesseract.image_to_string(img_dilation, config=config)
#printing the extracted text
print (text)
'''
