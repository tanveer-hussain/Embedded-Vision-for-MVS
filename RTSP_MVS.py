#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import threading
from threading import Thread
import time
import os
import numpy as np


####################################################
###   Entropy Computation   ####
####################################################

def entropy_main(img):

    size_img = img.shape
    rows = size_img[0]
    cols = size_img[1]
    size = rows * cols
    H = 0
    SV = 0
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert into HSV color space
    channels = cv2.split(hsv_img)  # seperate HSV channels
    hh = np.array(channels[0])  # take HUE
    ss = np.array(channels[1])  # take saturation
    hue = np.floor(np.multiply(hh, 8))  # quantize into 8 histogram bins
    sit = np.floor(np.multiply(ss, 2))  # quantize into 3 histogram bins
    hx = np.histogram(hue, bins=8)  # calculate hx, occurrance of each bin
    sx = np.histogram(sit, bins=3)  # calculate sx, occurrance of each bin
    px = np.divide(hx[0], size)  # calculuate probabilites by dividing each element in hx on size
    px1 = np.divide(sx[0], size)  # calculuate probabilites by dividing each element in sx on size
    for k in range(0, 8):
        H = H + -px[k] * np.log(px[k])  # calculate entropy for HUE component
    for k in range(0, 3):
        SV = SV + -px1[k] * np.log(px1[k])  # calculate entropy for Saturation and Value
    entropy_value = (H + SV) / 10

    return entropy_value


####################################################
###   Complexity Computation   ####
####################################################

def complexity_main(img1):

    (v, h, d) = img1.shape

    # print ('image shape from complexit = ', img1.shape)

    temp = v * h
    depth = 8
    bits = depth * temp
    sz1_img1 = bits / 8

    encode_param = [cv2.IMWRITE_PNG_COMPRESSION, 6]

    (compressed1, encimg1) = cv2.imencode('.jpg', img1, encode_param)

    # dec_img = cv2.imdecode(encimg1,1)
    # print ("depth of encimg = ", dec_img.dtype)

    (v1, h1) = encimg1.shape
    temp1 = v1 * h1
    depth1 = 8
    bits1 = depth1 * temp1
    sz2_img1 = bits1 / 8

    ratio1 = sz2_img1 / sz1_img1

    # print ('size 1 = ', sz1_img1, 'size 2 = ', sz2_img1, 'ratio =', ratio1)

    return ratio1


####################################################
###   Model Loading   ####
####################################################

def loadModel():
    classes = 'Models/coco.names'
    weights = 'Models/yolov3-tiny.weights'
    config = 'Models/yolov3-tiny.cfg'

    with open(classes, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    # print(classes)

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    # read pre-trained model and config file

    net = cv2.dnn.readNet(weights, config)
    return net


####################################################
###   Objects Detection   ####
####################################################

net = loadModel()


def tinu(image):

    def get_output_layers(net):

        layer_names = net.getLayerNames()

        output_layers = [layer_names[i[0] - 1] for i in
                         net.getUnconnectedOutLayers()]

        return output_layers

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    # create input blob

    blob = cv2.dnn.blobFromImage(
        image,
        scale,
        (416, 416),
        (0, 0, 0),
        True,
        crop=False,
        )

    # set input blob for the network

    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    # initialization

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)

            if class_id == 0:
                confidence = scores[class_id]

                if confidence > 0.5:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

    # apply non-max suppression

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold,
                               nms_threshold)

#    # go through the detections remaining
#    # after nms and draw bounding box
#

    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]

    return (image, confidences, class_ids)


def main():

    capture = cv2.VideoCapture('rtsp://admin:imlab3797@223.195.34.63:554/video1+audio1')

    #capture = cv2.VideoCapture(0)
    information_sum = []
    temp_images = []
    frame_writing_count = 0
    largestvalue = 0
    frames_count = 0

    while True:
        (status_i, frame) = capture.read()
        frame = cv2.resize(frame, (224, 224))
        frames_count += 1
        # cv2.imwrite('Test/Frame-'+ str(frames_count) + '.png', frame)
        # cv2.imshow(' ', frame)
        # cv2.waitKey(1)
        

        (annotated_frame, confidences, class_ids) = tinu(frame)

        if len(confidences) is not 0:
            if any([x > 0.7 for x in confidences]):
                persons = class_ids.count(0)
                print ('persons = ', persons)

                if persons >= 1:

                    entropy_value = entropy_main(frame)
                    complexity_value = complexity_main(frame)
                    #print ('entropy_value = ', entropy_value)
                    #print ('complexity_value = ', complexity_value)
                    temp_sum = entropy_value + complexity_value

                    information_sum.append(temp_sum)
                    temp_images.append(frame)
                    frame_writing_count += 1
                    #print ('frame_writing_count =', frame_writing_count)

                    if frame_writing_count >= 10:
                        frame_writing_count = 0
                        for (i, item) in enumerate(information_sum):
                            if item > largestvalue:
                                largestvalue = item
                                #print (' i = ' + str(i) + '   ### item = ' + str(item))
                                max_index1 = i
                                print (' max index = ' , max_index1)
                        path = 'Keyframes' + '/Keyframe-' + str(frames_count) + '.png'
                        cv2.imwrite(path, temp_images[max_index1])
                        temp_images = []
                        information_sum = []


        

main()
capture.release()

