# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:24:37 2020
@author: 1
"""
# from calc_indexes import *

import numpy as np
import matplotlib.pyplot as plt
import gc
import numpy as np


def obrez (hist, minHist, maxHist, percent):  
#    sum_per = 0 
#    hist_vos = []
    s = np.sum(hist)
    l = len(hist)
    procent = int(s*percent)
    print (procent, ' ', l)
    minIdx = 0
    maxIdx = l
    plus = 0
    for i in range (0, l):
        plus += hist[i]
        if plus >= procent:
            minIdx = i - 1
            break
    
    plus = 0
    l = l - 1
    for i in range (0, l):
        plus += hist[l - i]
        if plus >= procent:
            maxIdx = l - i
            break
    
    step = (maxHist - minHist)/(bins-1)
    
    minimum = minHist + minIdx * step
    maximum = minHist + (maxIdx + 1) * step
    
    print(minIdx, minimum)
    print(maxIdx, maximum)

    return minimum, maximum

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\Landsat_function.npy'
mas = np.load(folder)
MNDWI = mas[0]
# NDWI    = mas[2]
# AWEInsh = mas[1]
# AWEIsh  = mas[3]

bins = 100    

minMNDWI = np.min(MNDWI)
maxMNDWI = np.max(MNDWI)

print (minMNDWI,' ',maxMNDWI)

plt.title("MNDWI")

fMNDWI = MNDWI.ravel()
print(fMNDWI.shape)

h1 = np.histogram(fMNDWI, bins)
print(h1[0].shape)
# h1 = histogram(MNDWI, bins, minMNDWI, maxMNDWI)
plt.plot(h1[0])
plt.show()


minimum, maximum = obrez(h1[0], minMNDWI, maxMNDWI, 0.01)
print(minimum, maximum)
h2 = np.histogram(fMNDWI, bins,( minimum, maximum))

plt.title("MNDWI h2")
plt.plot(h2[0])
plt.show()


minimum, maximum = obrez(h2[0], minimum, maximum, 0.01)
h3 = np.histogram(fMNDWI, bins,( minimum, maximum))

plt.title("MNDWI h3")
plt.plot(h3[0])
plt.show()

h1 = None
h2 = None
gc.collect()

minimum, maximum = obrez(h3[0], minimum, maximum, 0.01)
h4 = np.histogram(fMNDWI, bins,( minimum, maximum))

plt.title("MNDWI h4")
plt.plot(h4[0])
plt.show()


minimum, maximum = obrez(h4[0], minimum, maximum, 0.01)
h5 = np.histogram(fMNDWI, bins,( minimum, maximum))

plt.title("MNDWI h5")
plt.plot(h5[0])
plt.show()

h4 = None
gc.collect()

minimum, maximum = obrez(h5[0], minimum, maximum, 0.01)
h6 = np.histogram(fMNDWI, bins,( minimum, maximum))

plt.title("MNDWI h6")
plt.plot(h6[0])
plt.show()


# print (np.max(NDWI),' ',np.min(NDWI))
# plt.title("NDWI")
# h2 = histogram(NDWI, 100, np.min(NDWI), np.max(NDWI))
# mi_ma = obrez(h2)


# print (np.max(AWEInsh),' ',np.min(AWEInsh))
# plt.title("AWEInsh")
# h3 = histogram(AWEInsh, 100, np.min(AWEInsh), np.max(AWEInsh))
# mi_ma = obrez(h3)


# print (np.max(AWEIsh),' ',np.min(AWEIsh))
# plt.title("AWEIsh")
# h4 = histogram(AWEIsh, 100, np.min(AWEIsh), np.max(AWEIsh))
# mi_ma = obrez(h4)



#AWEI = 4*(b3-b5)-(0.25*b5+2.75*b9)
#print (np.max(AWEI),' ',np.min(AWEI))
