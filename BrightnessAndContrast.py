# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:54:08 2022

@author: Plabo
"""


import cv2

im = cv2.imread("pic1.jpg")
#cv2.imshow('image',im)
#cv2.waitKey(0)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#gray = cv2.imread("scene.jpg", 0)

#size = gray.width * gray.height

print(gray)

size = 0
sum = 0
max = 0
min = 9999999999
for i in range (gray.shape[0]): #traverses through height of the image
    for j in range (gray.shape[1]): #traverses through width of the image
        sum = sum + gray[i][j]
        size=size+1
        
        if gray[i][j]>max:
            max= gray[i][j]
        if gray[i][j]<min:
            min=gray[i][j]
            

print("\n\nmax: ",max,"   min: ",min)
            

contrast = max - min
brightness =int(sum / size)
print("\nBrightness: ",brightness)
print("\nContrast: ",contrast)