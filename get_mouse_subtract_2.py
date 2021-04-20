import numpy as np
import cv2
import matplotlib.pyplot as plt # for plotting histogram
import os
import Constants as C

X=[]
Y=[]

Xblank=[]
Yblank=[]

   # mouse callback function
def mouse_callback(event,x,y,flags,param):
    global hsvImg
    global coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        X.append(x)
        Y.append(y)
        cv2.rectangle(hsvImg,
        (x,y),(x+C.W,y+C.W),
                (0,0,255),
                  1)
        coord = np.savetxt('xy_files/xy_values_'+str(os.path.split(C.img)[-1])+'.csv', (X,Y), fmt ='%f', delimiter = ',')


        print (x, y)
    if event == cv2.EVENT_RBUTTONDOWN:
        Xblank.append(x)
        Yblank.append(y)
        #coord=np.array([[x, y]])
        #coordinates=np.append(coordinates, coord, axis=0)
##        x,y,W,W = cv2.boundingRect()
        cv2.rectangle(hsvImg,
        (x,y),(x+C.W,y+C.W),
                (255,0, 0),
                  1)
        coord = np.savetxt('xy_files/xy_blank_values_'+str(os.path.split(C.img)[-1])+'.csv', (Xblank,Yblank), fmt ='%f', delimiter = ',')

imgOrig= cv2.imread(C.img)
#P Test
#imgOrig = cv2.imread(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/OAK_D_img -13-04-2021_12-04-05 frame.jpg')
#pH test
#imgOrig= cv2.imread(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/PXL_20210412_205759131~2.jpg')
imgsmall=cv2.resize(imgOrig,(1000, 400))
hsvImg= cv2.cvtColor(imgsmall,cv2.COLOR_BGR2HSV)
cv2.namedWindow("hsvImg") # Can be resized
cv2.setMouseCallback("hsvImg", mouse_callback) #Mouse callback
    
while True :
    cv2.imshow("hsvImg", hsvImg)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        cv2.destroyAllWindows()
        break
    

