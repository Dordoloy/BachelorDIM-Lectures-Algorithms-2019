# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:43:51 2019

@author: dordoloy
"""

#import numpy as np
import cv2
""" ---SLOW---
def invert_colors_manual(input_img):
    row = input_img.shape[0]
    col = input_img.shape[1]
    third_dim = input_img.shape[2]
    for i in range(row):
        for j in range(col):
            for k in range(third_dim):
                input_img[i,j,k] = 255 - input_img[i,j,k]
    return input_img
"""
img=cv2.imread('img/avatar.png',1)
print("BGR image shape = "+str(img.shape))
#display the loaded images cv2.imshow("Gray levels image", img_gray)


img=255-img
#output = invert_colors_manual(img)
#cv2.imshow("Reversed color Image",output)
#cv2.waitKey()
cv2.imshow("BGR image", img)
cv2.waitKey()