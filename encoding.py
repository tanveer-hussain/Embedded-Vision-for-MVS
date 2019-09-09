# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:50:31 2018

@author: Tanveer
"""

import cv2
import sys
import os

def encoding_image(img1):
    
    v, h, d = img1.shape
    temp = v * h
    depth = 8
    bits = depth * temp
    sz1_img1 = bits/8
    
    
    encode_param = [cv2.IMWRITE_PNG_COMPRESSION, 6]
    
    compressed1 , encimg1 = cv2.imencode('.jpg',img1, encode_param)

 
    return encimg1

