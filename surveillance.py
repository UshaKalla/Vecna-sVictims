import numpy as np 
import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt

# use camera
#cap = cv2.VideoCapture(0)
cap_mask=cv2.VideoCapture(0)

# import pretrained features
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# open camera and start reading
while True:
    #ret, frame = cap.read()
    ret_mask, frame_mask = cap_mask.read()

    # set the cascade frame to gray scale (requires gray scale to work)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame_mask, cv2.COLOR_BGR2HSV)
    
    # masking details
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1+mask2
    result = cv2.bitwise_and(frame_mask,frame_mask,mask=mask)


    # first parameter is scale factor (when resizing mask to find matches, smaller = more accurate but slower)
    # second parameter is minNeighbors (how many matches from training needed to count)
    #faces = face_cascade.detectMultiScale(gray,1.3,5) 

    # draw rectangles to indicate recognition
    # for (x,y,w,h) in faces:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5) # alias to original frame so be wary of changes
    #     roi_gray=gray[y:y+w,x:x+w] # region of interest, we'll check within the face rectangle for eyes
    #     roi_color = frame[y:y+w,x:x+w] # note [rows,columns]
    #     eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
    #     for (ex,ey,ew,eh) in eyes:
    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

    # cv2.imshow('frame',frame)
    cv2.imshow('masking',result)
    if cv2.waitKey(1)==ord('q'):
        break

# cap.release()
cap_mask.release()
cv2.destroyAllWindows()