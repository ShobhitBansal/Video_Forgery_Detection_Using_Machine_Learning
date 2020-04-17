import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import cv2
import numpy as np
from keras.models import load_model

vid_name = input("\nEnter the name of video: ")
vid_src = "G:/Video_Forgery_Detection_Using_Machine_Learning/Input_Videos/" + vid_name + ".mp4"
vid = []

sumFrames =0
fps = 0
cap= cv2.VideoCapture(vid_src)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        fps = cap.get(cv2.CAP_PROP_FPS)
        break
    sumFrames +=1
    vid.append(frame)
cap.release()
    
print("\nNo. Of Frames in the Video: ",sumFrames)

Xtest = np.array(vid)

print("\nPredicting !! ")
model = load_model("G:/Video_Forgery_Detection_Using_Machine_Learning/ResNet50_Model/forgery_model.hdf5")
output = model.predict(Xtest)

output = output.reshape((-1))
results = []
for i in output:
    if i>0.5:
        results.append(1)
    else:
        results.append(0)


no_of_forged = sum(results)
        
if no_of_forged < fps:
    print("\nThe video is not forged")
    
else:
    print("\nThe video is forged")
    print("\nNumber of Forged Frames in the video: ",no_of_forged)