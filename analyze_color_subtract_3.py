import numpy as np
import cv2
import os
import matplotlib.pyplot as plt # for plotting histogram
import Constants as C
#import image_quality_check as iqc
#import get_mouse_subtract as gms

##################################################################################
##import csv files and calculate average hsv values
##added sample csv file
##background correction not functional here

imgOrig= cv2.imread(C.img)
pc=np.genfromtxt(C.PIXEL_COORDINATES,delimiter=',', dtype="int")
spc = np.genfromtxt(C.SAMPLE_PIXEL_COORDINATES,delimiter=',', dtype="int")
#bpc=np.genfromtxt(C.BLANK_PIXEL_COORDINATES,delimiter=',', dtype="int")
imgsmall=cv2.resize(imgOrig,(1000, 400))
hsvImg= cv2.cvtColor(imgsmall,cv2.COLOR_BGR2HSV)

##################average HSV values for color chart selection#######################
h = []
s = []
v = []
for i in range(len(pc[0, :])):
    hi = hsvImg[pc[1, i]-C.W:pc[1, i]+C.W, pc[0, i]-C.W:pc[0, i]+C.W, 0] #2W by 2W HSV img
    h=np.append(h, int(np.average(hi)))
    si = hsvImg[pc[1, i]-C.W:pc[1, i]+C.W, pc[0, i]-C.W:pc[0, i]+C.W, 1] #2W by 2W HSV img   
    s=np.append(s,int(np.average(si)))
    vi = hsvImg[pc[1, i]-C.W:pc[1, i]+C.W, pc[0, i]-C.W:pc[0, i]+C.W, 2] #2W by 2W HSV img
    v=np.append(v, int(np.average(vi)))
coord = np.savetxt('HSV_files/HSV_values_'+str(os.path.split(C.PIXEL_COORDINATES)[-1])+'.csv', (h,s,v), fmt ='%f', delimiter = ',')


   
########################average HSV values for sample ##############################
hs=[]
ss=[]
vs=[]
for i in range(len(spc[0, :])):
    hsi = hsvImg[spc[1, i]-C.WS:spc[1, i]+C.WS, spc[0, i]-C.WS:spc[0, i]+C.WS, 0] #2W by 2W HSV img
    hs= np.append(hs, int(np.average(hsi)))
    ssi = hsvImg[spc[1, i]-C.WS:spc[1, i]+C.WS, spc[0, i]-C.WS:spc[0, i]+C.WS, 1] #2W by 2W HSV img   
    ss= np.append(ss, int(np.average(ssi)))
    vsi = hsvImg[spc[1, i]-C.WS:spc[1, i]+C.WS, spc[0, i]-C.WS:spc[0, i]+C.WS, 2] #2W by 2W HSV img
    vs= np.append(vs, int(np.average(vsi)))
coord = np.savetxt('Sample_HSV_files/Sample_HSV_values_'+str(os.path.split(C.PIXEL_COORDINATES)[-1])+'.csv', (hs,ss,vs), fmt ='%f', delimiter = ',')


#######################average HSV values for background#########################
hb = []
sb = []
vb= []
##for i in range(len(bpc[0, :])):
##    hblank = hsvImg[bpc[1, i]-C.W:bpc[1, i]+C.W, bpc[1, i]-C.W:bpc[1, i]+C.W, 0] #2W by 2W HSV img
##    hb.append(np.average(hblank))
##    sblank = hsvImg[bpc[1, i]-C.W:bpc[1, i]+C.W, bpc[1, i]-C.W:bpc[1, i]+C.W, 1] #2W by 2W HSV img
##    sb.append(np.average(sblank))
##    vblank = hsvImg[bpc[1, i]-C.W:bpc[1, i]+C.W, bpc[1, i]-C.W:bpc[1, i]+C.W, 2] #2W by 2W HSV img
##    vb.append(np.average(vblank))
##
##hbsample = np.array(hb)[-1] # for last column
##hb = np.array(hb)[:-1] # for all but last column
##sbsample = np.array(sb)[-1] # for last column
##sb = np.array(sb)[:-1] # for all but last column
##vbsample = np.array(vb)[-1] # for last column
##vb = np.array(vb)[:-1] # for all but last column
##


###uncomment for images separated in H, S, V space
##cv2.imshow("R", imgsmall[:,:,2])
##cv2.imshow("G",imgsmall[:, :, 1])
##cv2.imshow("B", imgsmall[:, :, 0])
###uncomment for images separated in B, G, R space
##cv2.imshow("H", hsvImg[:,:, 0])
##cv2.imshow("S", hsvImg[:, :, 1])
##cv2.imshow("V", hsvImg[:, :, 2])






