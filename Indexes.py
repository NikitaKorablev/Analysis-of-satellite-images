# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:24:37 2020
@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt


def histogram (array, bins, hmin, hmax):
    print(hmin, " ",hmax)
    hist = np.zeros(bins, dtype = np.uint32)
    step = (hmax - hmin)/(bins-1)
    for i in range (0, array.shape[0]):
        for m in range (0, array.shape[1]):
            if array[i,m] <= hmax and array[i,m] >= hmin:            
                indx = int((array[i,m] - hmin)//step)
                hist[indx] = hist[indx]+1
                  
    plt.plot(hist)
    plt.show()
    return hist

def obrez (hist, hmin, step):
    start = 0
    summa = 0
    procent = np.sum(hist) * 0.1
    for i in hist:
        start += 1
        summa += i
        if summa >= procent:
            break
    print(start-1)    
    new_hmin = hmin + (start-1)*step
    summa = 0
    for i in range (1, len(hist)):
        start = len(hist) - i
        summa += hist[start]
        if summa >= procent:
            break
    print(start+1)    
    new_hmax = hmin + (start + 1)*step
              
    return (new_hmin, new_hmax)
    
    
folder = r'D:\for_python_scripts\Nizni_chanels\Landsat_B'
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

bin_members = 300

""" MNDWI = (Blue − NIR)/(Blue + NIR) """
a = b2 - b5
b = b2 + b5
b[b == 0] = 1
MNDWI = np.divide(a,b)
min_MNDWI = np.min(MNDWI)
max_MNDWI = np.max(MNDWI)
step_MNDWI = (max_MNDWI - min_MNDWI)/(bin_members-1)
print (max_MNDWI,' ',min_MNDWI)
plt.title("MNDWI")
h1 = histogram(MNDWI, bin_members, min_MNDWI, max_MNDWI)

new_border_h1 = obrez(h1, min_MNDWI, step_MNDWI) 
h1_v2 = histogram(MNDWI, bin_members, new_border_h1[0], new_border_h1[1])

step = (new_border_h1[1] - new_border_h1[0]) / (bin_members-1)
new_border_h1 = obrez(h1_v2, new_border_h1[0], step)
h1_v3 = histogram(MNDWI, bin_members, new_border_h1[0], new_border_h1[1])

step = (new_border_h1[1] - new_border_h1[0]) / (bin_members-1)
new_border_h1 = obrez(h1_v2, new_border_h1[0], step)
h1_v4 = histogram(MNDWI, bin_members, new_border_h1[0], new_border_h1[1])



#""" NDWI = (Blue − Red)/(Blue + Red) """
#a = b2 - b4
#b = b2 + b4
#b[b == 0] = 1
#NDWI = np.divide(a,b)
#print (np.max(NDWI),' ',np.min(NDWI))
#plt.title("NDWI")
#h2 = histogram(NDWI, 100, np.min(NDWI), np.max(NDWI))
##h2_v2 = obrez(h2)



#""" AWEInsh = 4*(Blue - Near) - (0.25*Red + 2.75*SWIR2) """
#AWEInsh = 4*(b2 - b5) - (0.25*b4 + 2.75*b7)
#print (np.max(AWEInsh),' ',np.min(AWEInsh))
#plt.title("AWEInsh")
#h3 = histogram(AWEInsh, 100, np.min(AWEInsh), np.max(AWEInsh))
##h3_v2 = obrez(h3)



#""" AWEIsh = CA + 2.5*Blue - 1.5*(Red + Near) - 0.25*SWIR2 """
#AWEIsh = b1 + 2.5*b2 - 1.5*(b4 + b5) - 0.25*b7
#print (np.max(AWEIsh),' ',np.min(AWEIsh))
#plt.title("AWEIsh")
#h4 = histogram(AWEIsh, 100, np.min(AWEIsh), np.max(AWEIsh))
##h4_v2 = obrez(h4)





#AWEI = 4*(b3-b5)-(0.25*b5+2.75*b9)
#print (np.max(AWEI),' ',np.min(AWEI))
#проверка
