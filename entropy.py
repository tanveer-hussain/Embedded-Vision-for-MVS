# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:34:16 2018

@author: Tanveer
"""
import cv2
import numpy as np

def entropy_main(img):
    #print (img.shape)
    size_img = img.shape 
    rows = size_img[0]
    cols = size_img[1]
    size = rows*cols
    H = 0
    SV = 0  
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#convert into HSV color space
    channels = cv2.split(hsv_img)#seperate HSV channels
    hh = np.array(channels[0])#take HUE 
    ss = np.array(channels[1])#take saturation
    hue = np.floor(np.multiply(hh,8))#quantize into 8 histogram bins
    sit = np.floor(np.multiply(ss,2))#quantize into 3 histogram bins
    hx = np.histogram(hue,bins=8)#calculate hx, occurrance of each bin
    sx = np.histogram(sit,bins=3)#calculate sx, occurrance of each bin
    px = np.divide(hx[0],size)#calculuate probabilites by dividing each element in hx on size
    px1 = np.divide(sx[0],size)#calculuate probabilites by dividing each element in sx on size
    for k in range(0,8):
        H = H + (-px[k]*np.log(px[k]))#calculate entropy for HUE component
    for k in range(0,3):
        SV = SV + (-px1[k]*np.log(px1[k]))#calculate entropy for Saturation and Value
    entropy_value = (H + SV)/10
    
    return entropy_value







