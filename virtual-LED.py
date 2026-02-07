import numpy as np 
import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
import time
import plotly.express as px

LEDs = np.zeros(shape=72)
width = 12
height = 6

def get_col(index,width):
    return (int)(index/width)

def get_row(index,width):
    return index%width

def get_index(width,row,col):
    return width*row+col

def turn_on(width,row,col):
    plt.scatter(row+1,col+1,color='Yellow')
    time.sleep(10)
    plt.scatter(row+1,col+1,color='Gray')

# Plot first column as scatter points
index=0
while index<LEDs.size:
    plt.scatter(get_row(index, width)+1,get_col(index, width)+1, color="Gray")
    index=index+1
plt.xlim(0,14)
plt.ylim(0,8)
plt.title("LED Array")
plt.legend()

def graphUpdate(i):
    turn_on(width,3,4)


plt.show()

# while True:
#     turn_on(width,3,4)
#     time.sleep(10)




