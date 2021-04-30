import numpy as np
import cv2
import matplotlib.pyplot as plt # for plotting histogram
import os
import Constants as C

#################################################################################################################################################
##Insert a sample Image and use cv2.mouseEvents to click and select a rectangle of coordinates
## left click for color chart click
## for color chart make sure to click from least to most concentrated
## right click for sample 

X=[]
Y=[]

XSample=[]
YSample=[]

Xblank=[]
Yblank=[]

##mouse event function
def mouse_callback(event,x,y,flags,param):
    global hsvImg
    global coordinates
#left click for color chart--save as cvs file xy_values
    if event == cv2.EVENT_LBUTTONDOWN:
        X.append(x)
        Y.append(y)
        cv2.rectangle(hsvImg,
        (x,y),(x+C.W,y+C.W),
                (0,0,255),
                  1)
        coord = np.savetxt('xy_files/xy_values_'+str(os.path.split(img)[-1])+'.csv', (X,Y), fmt ='%f', delimiter = ',')
        print (x, y)

##right click click for sample--save as csv file xy_values_sample
    if event == cv2.EVENT_RBUTTONDOWN:
        XSample.append(x)
        YSample.append(y)
        cv2.rectangle(hsvImg,
        (x,y),(x+C.WS,y+C.WS),
                (0,255,0),
                  1)
        coord = np.savetxt('xy_files/xy_values_sample_'+str(os.path.split(img)[-1])+'.csv', (XSample,YSample), fmt ='%f', delimiter = ',')
        print (x, y)
##middle button click for background coordinates--save as csv file xy_values_blank      
    if event == cv2.EVENT_MBUTTONDOWN:
        Xblank.append(x)
        Yblank.append(y)
        cv2.rectangle(hsvImg,
        (x,y),(x+C.W,y+C.W),
                (255,0, 0),
                  1)
        coord = np.savetxt('xy_files/xy_blank_values_'+str(os.path.split(img)[-1])+'.csv', (Xblank,Yblank), fmt ='%f', delimiter = ',')
if isinstance(C.img, list)==True:
    for i in range(len(C.img)):
        img=C.img[i]
        imgOrig= cv2.imread(img)
        imgsmall=cv2.resize(imgOrig,(1000, 400))
        hsvImg= cv2.cvtColor(imgsmall,cv2.COLOR_BGR2HSV)
        cv2.namedWindow("hsvImg") # Can be resized
        cv2.setMouseCallback("hsvImg", mouse_callback) #Mouse callback

        ##click c if all coordinates have been collected    
        while True :
            cv2.imshow("hsvImg", hsvImg)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("c"):
                cv2.destroyAllWindows()
                break
else:
    img = C.img
    imgOrig= cv2.imread(img)


#P Test
#imgOrig = cv2.imread(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/OAK_D_img -13-04-2021_12-04-05 frame.jpg')
#pH test
#imgOrig= cv2.imread(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/PXL_20210412_205759131~2.jpg')
imgsmall=cv2.resize(imgOrig,(1000, 400))
hsvImg= cv2.cvtColor(imgsmall,cv2.COLOR_BGR2HSV)
cv2.namedWindow("hsvImg") # Can be resized
cv2.setMouseCallback("hsvImg", mouse_callback) #Mouse callback

##click c if all coordinates have been collected    
while True :
    cv2.imshow("hsvImg", hsvImg)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        cv2.destroyAllWindows()
        break
            


