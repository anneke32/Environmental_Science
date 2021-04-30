########Constants#########
from glob import glob
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
W=8
WS=16
import os

###################################choose either list of images or single image input#######################################################################
##img= []
##for filename in os.listdir(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images'):
##    if filename.endswith(".jpg"): 
##         img.append('images/'+filename)
##         continue
##    else:
##         continue
img = r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-13-25-04_N_white_indirect_surplus.jpg'


####################################choose either list of xy_files or single file input ########################################################################
##PIXEL_COORDINATES=[]
##for filename in os.listdir(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files'):
##   if filename.endswith(".csv"):
##            if filename.startswith("xy_values_O"):
##                PIXEL_COORDINATES.append('xy_files/'+filename)
##                continue
##            else:
##                continue
##
PIXEL_COORDINATES = r'xy_files/xy_values_OAK_D-04-19-13-25-04_N_white_indirect_surplus.jpg.csv'
##
##SAMPLE_PIXEL_COORDINATES=[]
##for filename in os.listdir(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files'):
##   if filename.endswith(".csv"):
##            if filename.startswith("xy_values_sample"):
##                SAMPLE_PIXEL_COORDINATES.append('xy_files/'+filename)
##                continue
##            else:
##                continue

SAMPLE_PIXEL_COORDINATES='xy_files/xy_values_sample_OAK_D-04-19-13-25-04_N_white_indirect_surplus.jpg.csv'




BLANK_PIXEL_COORDINATES= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_blank_values_OAK_D-04-19-15-07-47_K_white_indirect.jpg.csv'


