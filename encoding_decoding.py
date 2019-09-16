# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:50:31 2018

@author: Tanveer
"""

import cv2
import sys
import os

def encoding_image(img1):
    
    encode_param = [cv2.IMWRITE_PNG_COMPRESSION, 6]
    
    compressed1 , encimg1 = cv2.imencode('.jpg',img1, encode_param)

 
    return encimg1

def decoding_image(encimg):

    dec_img = cv2.imdecode(encimg,1)
    return dec_img

#enc_image = encoding_image(cv2.imread('1.png'))
#dec_image = decoding_image(enc_image)
#cv2.imwrite('decode.png', dec_image)



