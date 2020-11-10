# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:47:04 2020

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
import gc
from showIndexes import showNPY

def showHist(index, name):
    bins = 2000
    f_index = index.ravel()
    h1 = np.histogram(f_index, bins)
    print(name, f_index.shape)
    plt.title(name)
    plt.plot(h1[0])
    plt.show()

def showArr(arr, name):
    plt.title(name)
    plt.plot(arr)
    plt.show()
    
def calcIncreasingHist(index, bins):
    f_index = index.ravel()
    h = np.histogram(f_index, bins)
    inch = np.zeros(h[0].shape)
    inch[h[0].shape[0] - 1] = h[0][h[0].shape[0] - 1]
    for i in range(h[0].shape[0] - 2, -1, -1):
        inch[i] = h[0][i] + inch[i + 1]
    return (inch, h[1])

def findT(inch, water_pixels):
    t = -1
    for i in range(inch[0].shape[0] - 1, -1, -1):
        if(inch[0][i] == water_pixels):
            t = inch[1][i]
            break
        if(inch[0][i] > water_pixels):
            t = (inch[1][i] + inch[1][i + 1]) / 2
            break
    return t

def hists (folder):
    bins = 5000
    
    MNDWI   = np.load(folder + '/MNDWI.npy')
    mndwi_h = calcIncreasingHist(MNDWI, bins)
    showArr(mndwi_h[0], "MNDWI")
    
    print("TOTAL", MNDWI.shape[0] * MNDWI.shape[1])
    
    NDWI    = np.load(folder + '/NDWI.npy')
    ndwi_h  = calcIncreasingHist(NDWI, bins)
    showArr(ndwi_h[0], "NDWI")
    
    AWEInsh = np.load(folder + '/AWEInsh.npy')
    aweinsh_h = calcIncreasingHist(AWEInsh, bins)
    showArr(aweinsh_h[0], "AWEInsh")
    
    AWEIsh  = np.load(folder + '/AWEIsh.npy')
    aweish_h = calcIncreasingHist(AWEIsh, bins)
    showArr(aweish_h[0], "AWEIsh")
    
    MNDWI = None
    NDWI = None
    AWEInsh = None
    AWEIsh = None
    gc.collect()
    
    
    ndwi_t = 0.3877
    ndwi_idx = -1
    for i in range(ndwi_h[1].shape[0] - 1, -1, -1):
        if(ndwi_h[1][i] < ndwi_t):
            ndwi_idx = i + 1
            break
    
    ndwi_water = ndwi_h[0][i]
    print("NDWI WATER", ndwi_water)
    
    mndwi_t   = findT(mndwi_h, ndwi_water)
    aweinsh_t = findT(aweinsh_h, ndwi_water)
    aweish_t  = findT(aweish_h, ndwi_water)
    
    print("MNDWI THRESHOLD", mndwi_t)
    print("AWEInsh THRESHOLD", aweinsh_t)
    print("AWEIsh THRESHOLD", aweish_t)

    showNPY(folder, mndwi_t, ndwi_t, aweinsh_t, aweish_t)

    








