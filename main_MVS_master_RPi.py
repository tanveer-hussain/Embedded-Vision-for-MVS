# author@ tinu
# 23 Dec 2018 2:15 AM
from complexity import complexity_main
from entropy import entropy_main
import os
import numpy as np
import cv2
import shutil
import time
s_time = time.time()
def main():
        
        for dir_counter in range(1,43):
                all_sum = []
                image_list = []
                cout = 0
                largest1 = 0,
                largest2 = 0
                largest3 = 0
                largest4 = 0
                max_index1 = 0
                max_index2 = 0
                max_index3 = 0
                max_index4 = 0
                root_path = 'F:\\Research\\Multi View Video Summarization\\Pi based MVS\\Codes\\V4_final codes for summary generation Road dataset\\Master-RPi/' + str(dir_counter) + '/'
                dest = 'F:\\Research\\Multi View Video Summarization\\Pi based MVS\\Codes\\V4_final codes for summary generation Road dataset\\Master-RPi\\keyframes\\'
                for single_image in os.listdir(root_path):
                        #print ('Processing...' + root_path + single_image)
                        image = cv2.imread(root_path + single_image)
                        image_list.append(single_image)

                        entropy_value = entropy_main(image)
                        complexity_value = complexity_main(image)
                        

                        sum_values = entropy_value + complexity_value
                        all_sum.append(sum_values)



                        #print (str(cout),'Entropy score = ' , str(entropy_value), ', complexity score = ', str(complexity_value))
                        cout = cout + 1
                for i, item in enumerate(all_sum):
                        #print (all_sum[i])
                        if item > largest1:
                                largest1 = item
                                max_index1 = i
                        elif largest2 != largest1 and largest2 < item:
                                largest2 = item
                                max_index2 = i
                        elif largest3 != largest2 and largest2 != largest1 and largest3 < item:
                                largest3 = item
                                max_index3 = i
                        elif largest4 != largest3 and largest2 != largest1 and largest3 != largest2 and largest4 < item:
                                largest4 = item
                                max_index4 = i
                keyframe1 = image_list[int(max_index1)]
                keyframe2 = image_list[int(max_index2)]
                keyframe3 = image_list[int(max_index3)]
                keyframe4 = image_list[int(max_index4)]
                #print (max_index1,max_index2,max_index3,max_index4)
                #print (keyframe1,keyframe2,keyframe3,keyframe4)
                #print (largest1,largest2,largest3,largest4)

                shutil.copy(root_path+keyframe1, dest+keyframe1)
                shutil.copy(root_path+keyframe2, dest+keyframe2)
                shutil.copy(root_path+keyframe3, dest+keyframe3)
                shutil.copy(root_path+keyframe4, dest+keyframe4)
                print ('Processed.. ' + str(dir_counter))


                        
                        #cv2.imshow('Image', image)
                        #cv2.waitKey(3)


main()
e_time = time.time()
total_time = e_time - s_time
print ('total time = ', total_time)
