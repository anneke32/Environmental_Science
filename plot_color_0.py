import numpy as np
import cv2
import matplotlib.pyplot as plt # for plotting histogram
import analyze_color_subtract_5 as acs
import os
import Constants as C

#import get_mouse_subtract as gms
#try to add linear approximation
#split multidata array h into rows of 5
#


if len(acs.h)>12:
    h = np.reshape(acs.h, (13, 5))
    s = np.reshape(acs.s, (13, 5))
    v = np.reshape(acs.v, (13, 5))

else:
    h = acs.h
    s = acs.s
    v = acs.v




#print('color', color)
#plot colors
if len(acs.h)==7:
    conc= [4.5, 5, 5.5, 6, 6.5, 7, 7.5]
    my_xticks = ['Sample', 'pH 4.5','pH 5.0', 'pH 5.5', 'pH 6.0', 'pH 6.5', 'pH 7.0', 'pH 7.5']
    clog= conc
elif len(acs.h)==10:
    conc=[1/2, 1/4,1/8, 1/16 , 1/32, 1/64, 1/128, 1/256, 1/512, 1/1024]
    clog= np.absolute(np.log10(conc))
elif len(acs.h)==5:
    #conc= [i in range len(pc[1,:])]
    conc=[1, 2, 3, 4, 5]
    my_xticks = ['Depleted','Deficient','Adequate', 'Sufficient', 'Surplus']

    clog =conc
    
#sqrtSV = sqrt(V^2+S^2)




######figure of log concentration vs log(hsv/hsvblank)############################
##fig = plt.figure()
##plt.plot(clog, acs.vcrlog, label = "V log", marker = 'o')
##plt.plot(clog, acs.hcrlog, label = "H log", marker = 'o')
##plt.plot(clog, acs.scrlog, label = "S log", marker = 'o')
##plt.xlabel('log of concentration')
##plt.ylabel('log of HSV')
##plt.legend()
##plt.show()

######### figure concentration vs hsv #########################################
fig = plt.figure()
plt.scatter(conc, h, label = "H", marker='o', color= "green")
plt.scatter(conc, s, label = "S", marker='o', color ="red")
plt.scatter(conc, v, label= "V", marker='o', color= "blue")
plt.plot(acs.hs[2], label= 'sample H', marker='o', color = "lightgreen")
plt.plot(acs.ss[2], label = 'sample S', marker='o', color= "pink")
plt.plot(acs.vs[2], label = 'sample V', marker='o', color = "lightblue")
#####Linear fit for HSV
coefficient_h=np.polyfit(conc, h,1)
poly_h=np.poly1d(coefficient_h)
new_x_h = np.linspace(conc[0], conc[-1])
new_y_h = poly_h(new_x_h)
plt.plot(new_x_h, new_y_h, color="green")

coefficient_s= np.polyfit(conc, s, 1)
poly_s= np.poly1d(coefficient_s)
poly_sc= poly_s.c
print('equation:? ', poly_s.c)
print('x value: ', (acs.ss[2]-poly_s[1])/poly_s[0])
new_x_s = np.linspace(conc[0], conc[-1])
new_y_s = poly_s(new_x_s)
plt.plot(new_x_s, new_y_s, color="red")

coefficient_v= np.polyfit(conc, v, 1)
poly_v= np.poly1d(coefficient_v)
new_x_v = np.linspace(conc[0], conc[-1])
new_y_v = poly_v(new_x_v)
plt.plot(new_x_v, new_y_v, color="blue")

plt.xlabel('concentration')
plt.ylabel('HSV')
plt.title(str(os.path.split(C.PIXEL_COORDINATES)[-1]))
plt.xticks(conc, my_xticks)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=6)
plt.show()

#fig.savefig('plot_results/plot_new' + str(os.path.split(C.PIXEL_COORDINATES)[-1]) + '.png')

########## figure log concentration vs hsv ##################################
##fig = plt.figure()
##plt.plot(clog, acs.v, label = "V", marker = 'o')
##plt.plot(clog, acs.h, label = "H", marker = 'o')
##plt.plot(clog, acs.s, label = "S", marker = 'o')
##plt.xlabel('log of concentration')
##plt.ylabel('HSV')
##plt.legend()
##plt.show()
##fig.savefig('plot_results/plot_' + str(os.path.split(C.PIXEL_COORDINATES)[-1]) + '.png')
##
######################################plot of sample values###############################################
figs=plt.figure
plt.plot(acs.hs, label= 'sample H', marker='o', color = "lightgreen")
plt.plot(acs.ss, label = 'sample S', marker='o', color= "pink")
plt.plot(acs.vs, label = 'sample V', marker='o', color = "lightblue")
plt.ylabel('HSV')
plt.title('sample_values'+str(os.path.split(C.PIXEL_COORDINATES)[-1]))
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=6)
plt.show()
fig.savefig('plot_results/plot_sample_values_' + str(os.path.split(C.PIXEL_COORDINATES)[-1]) + '.png')

