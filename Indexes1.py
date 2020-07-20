# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:24:37 2020
@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt


def histogram (array, bins, hmin, hmax):
    hist = np.zeros(bins)
    step = (hmax - hmin)/(bins-1)
    
    for i in range (0, array.shape[0]):
        for m in range (0, array.shape[1]):
            if array[i,m] <= hmax and array[i,m] >= hmin:            
                indx = int((array[i,m] - hmin)//step)
                hist[indx] = hist[indx]+1
                  
    plt.plot(hist)
    plt.show()
    return hist


def hist_min_max (array, bins, imin, imax, hmin, hmax):
    hist = np.zeros(bins)
    step = (hmax - hmin)/(bins-1)
    hmin += step*imin
    hmax -= step*(len(hist)-imax)
    print (step, ' ', hmin, ' ', hmax)
    for i in range (0, array.shape[0]):
        for m in range (0, array.shape[1]):
            if array[i,m] <= hmax and array[i,m] >= hmin:            
                indx = int((array[i,m] - hmin)//step)
                hist[indx] = hist[indx]+1
                  
    plt.plot(hist)
    plt.show()
    return hist


def obrez (hist):  
#    sum_per = 0 
#    hist_vos = []
    sum = np.sum(hist)
    procent = int(sum*0.1)
    print (procent, ' ', len(hist))
    plus = 0
    for i in range (0, len(hist)):
        plus += hist[i]
        if plus >= procent:
            minimum = i - 1
            print (minimum)
            break
        
    plus = 0
    hist = hist[::-1]
    for i in range (0, len(hist)):
        plus += hist[i]
        if plus >= procent:
            maximum = len(hist) - i
            print (maximum)          
            break
    
    hist = hist[::-1]  

#    for n in hist:
#        sum_per += n
#        sum_per = float(sum_per)
#        hist_vos.append(sum_per)
#
#    plt.plot(hist_vos)
#    plt.show()
    return minimum, maximum

    
folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\REFLECTANCE\Landsat_B'
b1 = np.load(folder + '1.npy')
b2 = np.load(folder + '2.npy')
#b3 = np.load(folder + '3.npy')
b4 = np.load(folder + '4.npy')
b5 = np.load(folder + '5.npy')
#b6 = np.load(folder + '6.npy')
b7 = np.load(folder + '7.npy')
#b8 = np.load(folder + '8.npy')
#b9 = np.load(folder + '9.npy')
#b10 = np.load(folder + '10.npy')
#b11 = np.load(folder + '11.npy')



#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)

""" MNDWI = (Blue − NIR)/(Blue + NIR) """
a = b2 - b5
b = b2 + b5
b[b == 0] = 1
MNDWI = np.divide(a,b)
print (np.min(MNDWI),' ',np.max(MNDWI))
plt.title("MNDWI")
h1 = histogram(MNDWI, 100, np.min(MNDWI), np.max(MNDWI))

mi_ma = obrez(h1)
h1_v2 = hist_min_max(MNDWI, 100, mi_ma[0], mi_ma[1], np.min(MNDWI), np.max(MNDWI))



# """ NDWI = (Blue − Red)/(Blue + Red) """
# a = b2 - b4
# b = b2 + b4
# b[b == 0] = 1
# NDWI = np.divide(a,b)
# print (np.max(NDWI),' ',np.min(NDWI))
# plt.title("NDWI")
# h2 = histogram(NDWI, 100, np.min(NDWI), np.max(NDWI))
# mi_ma = obrez(h2)



# """ AWEInsh = 4*(Blue - Near) - (0.25*Red + 2.75*SWIR2) """
# AWEInsh = 4*(b2 - b5) - (0.25*b4 + 2.75*b7)
# print (np.max(AWEInsh),' ',np.min(AWEInsh))
# plt.title("AWEInsh")
# h3 = histogram(AWEInsh, 100, np.min(AWEInsh), np.max(AWEInsh))
# mi_ma = obrez(h3)



# """ AWEIsh = CA + 2.5*Blue - 1.5*(Red + Near) - 0.25*SWIR2 """
# AWEIsh = b1 + 2.5*b2 - 1.5*(b4 + b5) - 0.25*b7
# print (np.max(AWEIsh),' ',np.min(AWEIsh))
# plt.title("AWEIsh")
# h4 = histogram(AWEIsh, 100, np.min(AWEIsh), np.max(AWEIsh))
# mi_ma = obrez(h4)




#AWEI = 4*(b3-b5)-(0.25*b5+2.75*b9)
#print (np.max(AWEI),' ',np.min(AWEI))
