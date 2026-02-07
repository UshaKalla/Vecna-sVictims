import numpy as np 
import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt

# use camera
cap = cv2.VideoCapture(0)

# import pretrained features
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# open camera and start reading
while True:
    ret, frame = cap.read()

    # set the cascade frame to gray scale (requires gray scale to work)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # first parameter is scale factor (when resizing mask to find matches, smaller = more accurate but slower)
    # second parameter is minNeighbors (how many matches from training needed to count)
    faces = face_cascade.detectMultiScale(gray,1.3,5) 

    # draw rectangles to indicate recognition
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5) # alias to original frame so be wary of changes
        roi_gray=gray[y:y+w,x:x+w] # region of interest, we'll check within the face rectangle for eyes
        roi_color = frame[y:y+w,x:x+w] # note [rows,columns]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()