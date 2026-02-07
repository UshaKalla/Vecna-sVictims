import numpy as np 
import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
import time
import plotly.express as px

def get_col(index,width):
    return (int)(index/width)

def get_row(index,width):
    return index%width

def get_index(width,row,col):
    return width*row+col

def turn_on(width,row,col):
    plt.scatter(row+1,col+1,color='Yellow')

def turn_off(width,row,col):
    plt.scatter(row+1,col+1,color='Gray')

class LedArray:

    def __init__(self, width, height):
        self.LEDs = np.zeros(shape=72)
        self.width = 12
        self.height = 6

    def plot_leds(self): 
        index=0
        while index<self.LEDs.size:
            plt.scatter(get_row(index, self.width)+1,get_col(index, self.width)+1, color="Gray")
            index=index+1
        plt.xlim(0,14)
        plt.ylim(0,8)
        plt.title("LED Array")
        plt.legend()

        plt.tight_layout()
        plt.show(block=False)


    def graphUpdate(self,array,seconds):
        index = 0
        while index<self.width*self.height:
            row = get_row(index,self.width)
            col = get_col(index,self.width)
            if array[index]==1:
                print(f'turning on {row},{col}')
                plt.scatter(row+1,col+1,color='Yellow')
            else:
                print(f'turning off {row},{col}')
                plt.scatter(row+1,col+1,color='Gray')
            index=index+1
        
        plt.pause(seconds)
        plt.draw()
        # update graph
        #plt.draw()
        plt.pause(.1)

        # display graph
        plt.tight_layout()
        plt.show(block=False)




