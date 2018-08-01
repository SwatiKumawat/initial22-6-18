#!/usr/bin/python3

import cv2
import numpy as np
import pytesseract

img = cv2.imread("test3.jpg" ,cv2.IMREAD_GRAYSCALE)
img1 = cv2.multiply(img, 1.2)

kernel = np.ones((1,1), np.uint8)
erode = cv2.erode(img1,kernel,iterations=1)

cv2.imshow("image",img)
cv2.imshow("mul",img1)
cv2.imshow("erode",erode)
cv2.waitKey(0)

config = ('-l eng --oem 1 --psm 3')
#converting image text to string
text = pytesseract.image_to_string(erode, config=config)
#printing the extracted text
print (text)

'''
#say the text from image
engine=pyttsx3.init()
engine.say(text)
engine.runAndWait()
'''
