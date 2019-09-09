# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:03:29 2018

@author: imlab
"""
print ('Processing...')
import cv2
import threading
from threading import Thread
from yolo_main import tinu
import time
import os
s_time = time.time()
def video0():
    
    print ('Processing Video')
    #capture = cv2.VideoCapture('15 fps Office/office-0_15fps.avi')
#################
    
    capture = cv2.VideoCapture('Road_6FPS/0410_1_6fps.avi')

#################
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
#    fpss = capture.get(cv2.CAP_PROP_FPS)
    status_i , frame_i = capture.read()
    i = 1
    counter = 0
    vehicles = 0
    persons = 0
    sending_flag = 0
    shots_counter = 0
    shot_number = 0
    frames_count = 10
    while(i < total_frames - 1):
        
        sending_flag = sending_flag + 1
        if sending_flag >= 3:
            sending_flag = 0
            image, confidences, class_ids = tinu(frame_i)
            
            #print ('**',confidences)
            #cv2.imshow('Frame',image)
            if len(confidences) is not 0:
                if any([x > 0.7 for x in confidences]):
                    cycle = class_ids.count(1)
                    car = class_ids.count(2)
                    bike = class_ids.count(3)
                    bus = class_ids.count(5)
                    train = class_ids.count(6)
                    truck = class_ids.count(7)
                    vehicles = cycle + car + bike + bus + train + truck
                    persons = class_ids.count(0)
                    #print ('persons = ' , persons, 'vehicles = ', vehicles)
                    #print ('**',confidences,'##')
                    if (vehicles >= 4 and persons >= 2) or (vehicles >= 3 and persons >= 3) or (vehicles >= 5) or (persons >= 5):
                        frames_count = frames_count + 1
                        if frames_count >= 10:
                            frames_count = 0
                            shot_number = shot_number + 1
                            shots_path = 'Master-RPi/' + str(shot_number)
                            if os.path.exists(shots_path):
                                pass
                            else:

                                os.mkdir(shots_path)
###############
                        path = 'Master-RPi/' + str(shot_number) + '/frame_' + str(i) + '_v1.png'
###############
                        cv2.imwrite(path,frame_i)
                        print ('Frame written at: ', path)
                        #cv2.imshow('f',image)
                        #cv2.waitKey(30)
                    
                    vehicles = 0
                    persons = 0
        status_i , frame_i = capture.read()
        #copy = frame_i
        k = cv2.waitKey(30) & 0xff
        i = i + 1
        if k == 27:
            break
    print ('Processing Video 0 done')
        
video0()
#	
#threads = 16  # Number of processes to create

#jobs = []
#
#thread0 = threading.Thread(target=video0)
#jobs.append(thread0)
#
#thread1 = threading.Thread(target=video1)
#jobs.append(thread1)
#
#thread2 = threading.Thread(target=video2)
#jobs.append(thread2)

#thread3 = threading.Thread(target=video3)
#jobs.append(thread3)
#
#
#for j in jobs:
 #   j.start()
#    
#for j in jobs:
#    
#    j.join()
#    
e_time = time.time()
total_time = e_time - s_time
print ('total time = ', total_time)
