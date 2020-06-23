# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:24:37 2020
@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt


def histogram (array, bins):
    hist = np.zeros(bins)
#    hist_min = []
#    sum_per = 0
    hmin = np.min(array)
    hmax = np.max(array)
    step = (hmax - hmin)/(bins-1)
    for i in range (0, array.shape[0]):
        for m in range (0, array.shape[1]):
            indx = int((array[i,m] - hmin)//step)
            hist[indx] = hist[indx]+1
#    plt.hist(hist, density=False, bins=200)
                  
    plt.plot(hist)
    plt.show()
# восходящая с минимумом
    
    sum = np.sum(hist)
    procent = int(sum*0.05)
    print (procent, ' ', len(hist))
    plus = 0
    
    for i in range (0, len(hist)):
        plus += hist[i]
        if plus >= procent:
            print (i)
            hist = hist[(i-1):]
            break
    
    plus = 0
    
    hist = hist[::-1]
    
    for i in range (0, len(hist)):
        plus += hist[i]
        if plus >= procent:
            print (i)
            hist = hist[(i-1):]
            break

    hist = hist[::-1]  
    
#    for i in range (0, len(hist)):
#        m = len(hist)-i
#        plus += hist[m]
#        if plus >= procent:
#            print (m)
#            hist = hist[:m]
#            break
#    for n in hist:
#        sum_per += n
#        if sum_per > procent:
#            sum_per = float(sum_per)
#            hist_min.append(sum_per)

    plt.plot(hist)
    plt.show()
    
    return hist


    
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

""" MNDWI = (Blue − NIR)/(Blue + NIR) """
a = b2 - b5
b = b2 + b5
b[b == 0] = 1
MNDWI = np.divide(a,b)
print (np.max(MNDWI),' ',np.min(MNDWI))
h1 = histogram(MNDWI, 100)


""" NDWI = (Blue − Red)/(Blue + Red) """
a = b2 - b4
b = b2 + b4
b[b == 0] = 1
NDWI = np.divide(a,b)
print (np.max(NDWI),' ',np.min(NDWI))
h2 = histogram(NDWI, 100)


""" AWEInsh = 4*(Blue - Near) - (0.25*Red + 2.75*SWIR2) """
AWEInsh = 4*(b2 - b5) - (0.25*b4 + 2.75*b7)
print (np.max(AWEInsh),' ',np.min(AWEInsh))
h3 = histogram(AWEInsh, 100)


""" AWEIsh = CA + 2.5*Blue - 1.5*(Red + Near) - 0.25*SWIR2 """
AWEIsh = b1 + 2.5*b2 - 1.5*(b4 + b5) - 0.25*b7
print (np.max(AWEIsh),' ',np.min(AWEIsh))
h4 = histogram(AWEIsh, 100)




#AWEI = 4*(b3-b5)-(0.25*b5+2.75*b9)
#print (np.max(AWEI),' ',np.min(AWEI))
#проверка
