# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:50:31 2018

@author: Tanveer
"""

import cv2
import sys
import os

def decoding_image(encimg1):
    
    dec_img = cv2.imdecode(encimg1,1)

 
    return dec_img

