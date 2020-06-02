# Intelligent Embedded Vision for Summarization of Multi-View Videos in IIoT

## Paper
https://ieeexplore.ieee.org/document/8815938

## Notice
Prior to the codes usage for industrial purposes or re-distribution, please read the licensing information given at the end of  <b> README file </b>



## How to Run? 
A step-wise tutorial explaining functionality of this code can be found here at links below (Part 1 and 2):
 - https://www.youtube.com/watch?v=SDq_5ZbTbqo
 - https://www.youtube.com/watch?v=aHvTtb8MbnQ
 
## Demo Video
 - https://www.youtube.com/watch?v=NAFx9S9v6Co


# Repository Explaination
There are total six Python script files and one two other folders [Models, suspicious-objects-detection] in this repository (Explained alphabetically).

### 1. complexity.py

It returns a single flot value which is used in "main_MVS_master_RPi.py" for summary generation.

### 2. encoding_decoding.py

This file has two functions where [encoding_image] takes input image and returns an encoded image and the function [decoding_image] function takes and decodes it into normal RGB format image.

### 3. entropy.py

It computes information inside image and returns a float value. It's input argument is image.

### 4. main_MVS_master_RPi.py

It receives frames for a certain duration from client RPis, decodes them and computes information by calling entropy and complexity functions and finally writes keyframes.

### 5. shots_segmentation_client_RPi.py

This code is executed over client RPis where a real-time video is captured, annotated, encoded and transmitted over WSN to master RPi.

### 6. yolo_main.py

This file takes input image and returns confidence scores and locations of detected objects.

## Models

Trained weights for tiny yolo can be downloaded from given link:
- https://pjreddie.com/darknet/yolo/

## suspicious-objects-detection

For custom object detection we retrained yolov3-tiny model for our own types of object i.e., suspicious ones that include gun, pistols, and knives. For annotating objects, first we downloaded different pictures from Google with several queries and take screenshots from some YouTube videos and movies. The overall training images were only 105 due to no public availability of such kind of dataset. Therefore, the trained model does not work well with every type of images.
The screenshot for average loss through out training process is given below:

![tiny-yolo-0 05-loss](https://user-images.githubusercontent.com/40714349/64930457-e49b6400-d86b-11e9-9635-a5dd00e25b24.png)

#### Final training loss is 0.06

##### Some sample results are given below:

![suspicious-results JPG](https://user-images.githubusercontent.com/40714349/64930635-a0a95e80-d86d-11e9-9b85-c5464df75b3a.png)

For trained model please follow the below links:

- https://drive.google.com/open?id=1hBCuJsGl6XhFS-oDGOmpddrZrYYvLGic
- https://drive.google.com/open?id=1Lpp4zXTuvTEbi0p6heHnjbSD3OiyTLtO


## Outsourcing and Licensing
<license>
 Copyright (c) 2019 "copyright notice checker" Authors. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer. <br />

* Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution. <br />
* None of the names of its contributors may be used to endorse
or promote products derived from this software without specific
prior written permission. <br />

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
</license>

# Citation
<pre>
<code>
Hussain, T., Muhammad, K., Del Ser, J., Baik, S. W., & de Albuquerque, V. H. C. (2019). Intelligent Embedded Vision for Summarization of Multi-View Videos in IIoT. IEEE Transactions on Industrial Informatics.
</code>
</pre>

If you are interested in Video Summarization domain you may find some of my other recent papers worthy to read:

<pre>
<code>
K. Muhammad, T. Hussain, and S. W. Baik, "Efficient CNN based summarization of surveillance videos for resource-constrained devices," Pattern Recognition Letters, 2018/08/07/ 2018

Hussain, Tanveer, Khan Muhammad, Amin Ullah, Zehong Cao, Sung Wook Baik, and Victor Hugo C. de Albuquerque. "Cloud-Assisted Multi-View Video Summarization using CNN and Bi-Directional LSTM." IEEE Transactions on Industrial Informatics (2019).

K. Muhammad, T. Hussain, M. Tanveer, G. Sannino and V. H. C. de Albuquerque, "Cost-Effective Video Summarization using Deep CNN with Hierarchical Weighted Fusion for IoT Surveillance Networks," in IEEE Internet of Things Journal.
doi: 10.1109/JIOT.2019.2950469

K. Muhammad, H. Tanveer, J. Del Ser, V. Palade and V. H. C. De Albuquerque, "DeepReS: A Deep Learning-based Video Summarization Strategy for Resource-Constrained Industrial Surveillance Scenarios," in IEEE Transactions on Industrial Informatics.
doi: 10.1109/TII.2019.2960536
keywords: {Big Data;Computer Vision;Deep Learning;Video Summarization;IIoT;Resource-Constrained Devices},
URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8936419&isnumber=4389054
</code>
</pre>
