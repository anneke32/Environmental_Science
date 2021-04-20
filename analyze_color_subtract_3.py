import numpy as np
import cv2
import matplotlib.pyplot as plt # for plotting histogram
import Constants as C
#import get_mouse_subtract as gms
#try to add linear approximation

imgOrig= cv2.imread(C.img)
pc=np.genfromtxt(C.PIXEL_COORDINATES,delimiter=',', dtype="int")
bpc=np.genfromtxt(C.BLANK_PIXEL_COORDINATES,delimiter=',', dtype="int")
imgsmall=cv2.resize(imgOrig,(1000, 400))
hsvImg= cv2.cvtColor(imgsmall,cv2.COLOR_BGR2HSV)


#cv2.imshow("H", hsvImg[:,:, 0])
#cv2.imshow("S", hsvImg[:, :, 1])
#cv2.imshow("V", hsvImg[:, :, 2])

h = []
s = []
v = []


for i in range(len(pc[0, :])):
    hi = hsvImg[pc[1, i]-C.W:pc[1, i]+C.W, pc[0, i]-C.W:pc[0, i]+C.W, 0] #2W by 2W HSV img
    h.append(np.average(hi))
    si = hsvImg[pc[1, i]-C.W:pc[1, i]+C.W, pc[0, i]-C.W:pc[0, i]+C.W, 1] #2W by 2W HSV img   
    s.append(np.average(si))
    vi = hsvImg[pc[1, i]-C.W:pc[1, i]+C.W, pc[0, i]-C.W:pc[0, i]+C.W, 2] #2W by 2W HSV img
    v.append(np.average(vi))

hsample = np.array(h)[-1] # for last column
h = np.array(h)[:-1] # for all but last column
ssample = np.array(s)[-1] # for last column
s = np.array(s)[:-1] # for all but last column
vsample = np.array(v)[-1] # for last column
v = np.array(v)[:-1] # for all but last column




hb = []
sb = []
vb= []

for i in range(len(bpc[0, :])):
    hblank = hsvImg[bpc[1, i]-C.W:bpc[1, i]+C.W, bpc[1, i]-C.W:bpc[1, i]+C.W, 0] #2W by 2W HSV img
    hb.append(np.average(hblank))
    sblank = hsvImg[bpc[1, i]-C.W:bpc[1, i]+C.W, bpc[1, i]-C.W:bpc[1, i]+C.W, 1] #2W by 2W HSV img
    sb.append(np.average(sblank))
    vblank = hsvImg[bpc[1, i]-C.W:bpc[1, i]+C.W, bpc[1, i]-C.W:bpc[1, i]+C.W, 2] #2W by 2W HSV img
    vb.append(np.average(vblank))

hbsample = np.array(hb)[-1] # for last column
hb = np.array(hb)[:-1] # for all but last column
sbsample = np.array(sb)[-1] # for last column
sb = np.array(sb)[:-1] # for all but last column
vbsample = np.array(vb)[-1] # for last column
vb = np.array(vb)[:-1] # for all but last column

hcr=[]
scr=[]
vcr=[]

#if bpc True:
hcr=np.divide(h, hb)
scr=np.divide(s,sb)
vcr = np.divide(v, vb)
##    else:
##        hcr = h
##        scr = s
##        vcr = v

vcrlog = np.log10(vcr)
hcrlog = np.log10(hcr)
scrlog = np.log10(scr)





