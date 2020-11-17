# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:08:58 2020

@author: basyr
"""

import numpy as np
import matplotlib.pyplot as plt
import gc
from calc_indexes import *

folder = r'D:\indexes\Landsat_B'
b1 = np.load(folder + '1.npy')
b2 = np.load(folder + '2.npy')
b4 = np.load(folder + '4.npy')
b5 = np.load(folder + '5.npy')
b7 = np.load(folder + '7.npy')

MNDWI = getMNDWI(b2, b5)
T = 0.3877
MNDWI[MNDWI >= T] = 1
MNDWI[MNDWI < T] = 0

NDWI    = getNDWI(b2, b4)
T = 0.3877
NDWI[NDWI >= T] = 1
NDWI[NDWI < T] = 0


AWEInsh = getAWEInsh(b2, b4, b5, b7)
T = 0.1897
AWEInsh[AWEInsh >= T] = 1
AWEInsh[AWEInsh < T] = 0


AWEIsh  = getAWEIsh(b1, b2, b4, b5, b7)
T = 0.1897
AWEIsh[AWEIsh >= T] = 1
AWEIsh[AWEIsh < T] = 0


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