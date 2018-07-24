#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:08:35 2018

@author: pallavi
"""

import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('input_videos/dance.mp4')
success,image = vidcap.read()
count = 0
success = True
c3=0
while success:
  if(c3%3==0): #taking every 3rd frame
      cv2.imwrite("images_dance/frame%d.jpg" % count, image) 
      count += 1
      print(count)
      # save frame as JPEG file
  c3+=1
  success,image = vidcap.read()
  
  
