# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:08:58 2020

@author: basyr
"""

import numpy as np
import matplotlib.pyplot as plt

def showNPY(folder, mndwi_t, ndwi_t, aweinsh_t, aweish_t):
    MNDWI   = np.load(folder + '/MNDWI.npy')
    NDWI    = np.load(folder + '/NDWI.npy')
    AWEInsh = np.load(folder + '/AWEInsh.npy')
    AWEIsh  = np.load(folder + '/AWEIsh.npy')

    # T = 0.3877
    MNDWI[MNDWI >= mndwi_t] = 1
    MNDWI[MNDWI < mndwi_t]  = 0
    
    # T = 0.3877
    NDWI[NDWI >= ndwi_t] = 1
    NDWI[NDWI < ndwi_t]  = 0
    
    # T = 0.1897
    AWEInsh[AWEInsh >= aweinsh_t] = 1
    AWEInsh[AWEInsh < aweinsh_t]  = 0
    
    # T = 0.1897
    AWEIsh[AWEIsh >= aweish_t] = 1
    AWEIsh[AWEIsh < aweish_t]  = 0
    
    
    plt.figure(figsize=(20,10))
    plt.title("MNDWI")
    plt.imshow(MNDWI, 'Greys')
    
    plt.figure(figsize=(20,10))
    plt.title("NDWI")
    plt.imshow(NDWI, 'Greys')
    
    plt.figure(figsize=(20,10))
    plt.title("AWEInsh")
    plt.imshow(AWEInsh, 'Greys')
    
    plt.figure(figsize=(20,10))
    plt.title("AWEIsh")
    plt.imshow(AWEIsh, 'Greys')