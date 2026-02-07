import numpy as np 
import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt


class Camera:

    def __init__(self, cap):
        self.cap=cap
        self.redmask=np.zeros(shape=(1,1))
        self.cam_width=0
        self.cam_height=0

    def camera_on(self):
        # open camera and start reading
        while True:
            ret_mask, frame_mask = self.cap.read()
            self.cam_width=(int)(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.cam_height=(int)(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

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
            result = cv2.bitwise_and(frame_mask,frame_mask,mask=mask)

            cv2.imshow('masking',result)

            # include LEDmask in object class
            # scaledmask = scale_mask(cam_width,cam_height,12,6,mask)
            self.redmask=mask.copy()

            if cv2.waitKey(1)==ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def scale_mask(width,height,scale_width,scale_height,mask):
        scaled_m=np.zeros(shape=(scale_width,scale_height))
        x=(int)(width/scale_width)+.5
        y=(int)(height/scale_height)
        print(f'width,height = {width},{height}')
        print(f'(x,y)=({x},{y})')
        i=0
        j=0
        while i<(height):
            while j<(width):
                scaled_row = (int)(j/x)
                scaled_col = (int)(i/y)
                scaled_m[scaled_row,scaled_col]+=mask[i,j]
                j=j+1
            j=0
            i=i+1

        i=0
        j=0
        while i<(scale_height):
            while j<(scale_width):
                scaled_m[i,j]=scaled_m[i,j]/(x*y)
                j=j+1
            j=0
            i=i+1

        i=0
        j=0
        while i<(scale_height):
            while j<(scale_width):
                if scaled_m[i,j]>0.5:
                    scaled_m[i,j]=1
                else:
                    scaled_m[i,j]=0
                j=j+1
            j=0
            i=i+1
        return scaled_m


