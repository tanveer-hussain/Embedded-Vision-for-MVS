# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:50:31 2018

@author: Tanveer
"""

import cv2
import sys
import os

def complexity_main(img1):
    
    v, h, d = img1.shape
    temp = v * h
    depth = 8
    bits = depth * temp
    sz1_img1 = bits/8
    
    
    encode_param = [cv2.IMWRITE_PNG_COMPRESSION, 6]
    
    compressed1 , encimg1 = cv2.imencode('.jpg',img1, encode_param)
    #dec_img = cv2.imdecode(encimg1,1)
    #print ("depth of encimg = ", dec_img.dtype)
    
    v1, h1 = encimg1.shape
    temp1 = v1 * h1
    depth1 = 8
    bits1 = depth1 * temp1
    sz2_img1 = bits1/8
        
    ratio1 = (sz2_img1/sz1_img1)
    #print ('size 1 = ', sz1_img1, 'size 2 = ', sz2_img1)

 
    return ratio1

#print ('complexity = ', information(cv2.imread('Shots/v0/frame_12_v0.png')))
#print ('complexity = ', information(cv2.imread('amir.png')))
