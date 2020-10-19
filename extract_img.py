# -- extract imgs from a video

import cv2
import os


video_path = "D:/Parking_data/B1/cam15/cam15_person.avi"

cap = cv2.VideoCapture(video_path)
Video_Lenght = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Video Lenght: "+str(Video_Lenght))
img_folder = "D:/Parking_data/B1/cam15/cam15/"
print("Img Folder: " + img_folder)
if not os.path.exists(img_folder):
    os.mkdir(img_folder)
for FrameCnt in range(Video_Lenght):
    success,img = cap.read()
    if(success):
        print("Frame:"+str(FrameCnt))
        img_name = "Cam15_" + "0"*(len(str(Video_Lenght))-len(str(FrameCnt)))+str(FrameCnt)+".jpg"
        img_path = os.path.join(img_folder,img_name)
        #print("Image path "+img_path)
        cv2.imwrite(img_path,img)
    else:
        print("Couldnt read frame "+str(FrameCnt))
