# author@ tinu
# 15 Sep 2019 8:26 PM

import os
import numpy as np
import cv2
import shutil
import time
from yolo_main import tinu

def object_detector():

        input_image = cv2.imread('images/suspicious-31.JPEG')
        image, confidences, class_ids = tinu(input_image)
        print ('Class ID = ', class_ids, ', Confidence = ', confidences)
        cv2.imshow('Output', image)
        cv2.waitKey(0)

object_detector()

        
        
