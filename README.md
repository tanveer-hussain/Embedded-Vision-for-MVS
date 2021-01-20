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

Contact Me
========
If you feel any difficulty or errors, please refer to tanveerkhattak37973[at][gmail]

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
@article{hussain2019intelligent,
  title={Intelligent Embedded Vision for Summarization of Multiview Videos in IIoT},
  author={Hussain, Tanveer and Muhammad, Khan and Del Ser, Javier and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={4},
  pages={2592--2602},
  year={2019},
  publisher={IEEE}
}
</code>
</pre>

If you are interested in Multi-view Video Summarization domain you may want to read our recent survey:

<pre>
<code>
@article{hussain2020comprehensive,
  title={A comprehensive survey of multi-view video summarization},
  author={Hussain, Tanveer and Muhammad, Khan and Ding, Weiping and Lloret, Jaime and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={Pattern Recognition},
  volume={109},
  pages={107567},
  year={2020},
  publisher={Elsevier}
}
</code>
</pre>

### My further research [sorted year-wise] on Video Summarization (single- and multi-view video summarization) domain is as follows:
#### Multi-view Video Summarization
<pre>
<code>
@ARTICLE{9208765,
  author={T. {Hussain} and K. {Muhammad} and A. {Ullah} and J. {Del Ser} and A. H. {Gandomi} and M. {Sajjad} and S. W. {Baik} and V. H. C. {de Albuquerque}},
  journal={IEEE Internet of Things Journal}, 
  title={Multi-View Summarization and Activity Recognition Meet Edge Computing in IoT Environments}, 
  year={2020},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/JIOT.2020.3027483}}
@article{hussain2019intelligent,
  title={Intelligent Embedded Vision for Summarization of Multiview Videos in IIoT},
  author={Hussain, Tanveer and Muhammad, Khan and Del Ser, Javier and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={4},
  pages={2592--2602},
  year={2019},
  publisher={IEEE}
}
@article{hussain2019cloud,
  title={Cloud-assisted multiview video summarization using CNN and bidirectional LSTM},
  author={Hussain, Tanveer and Muhammad, Khan and Ullah, Amin and Cao, Zehong and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={1},
  pages={77--86},
  year={2019},
  publisher={IEEE}
}
@article{후세인2018구조적인,
  title={구조적인 유사성에 기반한 다중 뷰 비디오의 효율적인 키프레임 추출},
  author={후세인 and 탄베르 and 칸살만 and 이미영 and 백성욱 and others},
  journal={한국차세대컴퓨팅학회 논문지},
  volume={14},
  number={6},
  pages={7--14},
  year={2018}
}
</code>
</pre>


#### Single-view Video Summarization
<pre>
<code>
@article{muhammad2020efficient,
  title={Efficient and Privacy Preserving Video Transmission in 5G-Enabled IoT Surveillance Networks: Current Challenges and Future Directions},
  author={Muhammad, Khan and Hussain, Tanveer and Rodrigues, Joel JPC and Bellavista, Paolo and de Macedo, Antonio Roberto L and de Albuquerque, Victor Hugo C},
  journal={IEEE Network},
  year={2020},
  publisher={IEEE}
}
@article{muhammad2020efficient,
  title={Efficient CNN based summarization of surveillance videos for resource-constrained devices},
  author={Muhammad, Khan and Hussain, Tanveer and Baik, Sung Wook},
  journal={Pattern Recognition Letters},
  volume={130},
  pages={370--375},
  year={2020},
  publisher={Elsevier}
}
@article{muhammad2019deepres,
  title={DeepReS: A Deep Learning-Based Video Summarization Strategy for Resource-Constrained Industrial Surveillance Scenarios},
  author={Muhammad, Khan and Hussain, Tanveer and Del Ser, Javier and Palade, Vasile and De Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={9},
  pages={5938--5947},
  year={2019},
  publisher={IEEE}
}
@article{muhammad2019cost,
  title={Cost-effective video summarization using deep CNN with hierarchical weighted fusion for IoT surveillance networks},
  author={Muhammad, Khan and Hussain, Tanveer and Tanveer, Muhammad and Sannino, Giovanna and de Albuquerque, Victor Hugo C},
  journal={IEEE Internet of Things Journal},
  volume={7},
  number={5},
  pages={4455--4463},
  year={2019},
  publisher={IEEE}
}
</code>
</pre>
