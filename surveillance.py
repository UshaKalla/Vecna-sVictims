import numpy as np 
import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt


def camera_on():
    # use camera
    cap_mask=cv2.VideoCapture(0)

    # open camera and start reading
    while True:
        ret_mask, frame_mask = cap_mask.read()

        # set the cascade frame to gray scale (requires gray scale to work)
        gray = cv2.cvtColor(frame_mask, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame_mask, cv2.COLOR_BGR2HSV)
        
        # masking details
        lower_red1 = np.array([0, 120, 120])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([160, 120, 120])
        upper_red2 = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1+mask2
        print(mask)
        result = cv2.bitwise_and(frame_mask,frame_mask,mask=mask)

        cv2.imshow('masking',result)
        if cv2.waitKey(1)==ord('q'):
            break

    cap_mask.release()
    cv2.destroyAllWindows()

def scale_mask(w,h):
    scaled_m=np.zeros(shape=w*h)

