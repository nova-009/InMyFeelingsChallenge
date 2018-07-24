#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:36:52 2018

@author: pallavi
"""

import cv2


for i in range(8,47952):
    img = cv2.imread('images_dance/frame'+str(i)+'.jpg',cv2.IMREAD_GRAYSCALE)
    ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    small = cv2.resize(thresh1, (0,0), fx=0.5, fy=0.5)
    cv2.imwrite('output_images/frame'+str(i-8)+'.jpg',small)
    print(i)
    
    