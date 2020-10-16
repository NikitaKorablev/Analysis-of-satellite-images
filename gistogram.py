# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:47:04 2020

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
import gc
import numpy as np

def hist1 (index, bins, name):
    
    plt.title(name)
    
    f_index = index.ravel()
    print(f_index.shape)
    
    index = None
    gc.collect()
    
    h1 = np.histogram(f_index, bins)
    print('shape: ', h1[0].shape)
    plt.plot(h1[0])
    plt.show()
    
    return h1
    
bins = 2000

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\MNDWI.npy'
t = 'MNDWI'
MNDWI = np.load(folder)
f_index = hist1(MNDWI, bins, t)
b = f_index[0][245:265]
plt.title('MNDWI_2')
plt.plot(b)
plt.show()

f_index = None
MNDWI = None
gc.collect()

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\AWEInsh.npy'
t = 'AWEInsh'
AWEInsh = np.load(folder)
f_index = hist1(AWEInsh, bins, t)
b = f_index[0][203:310]
plt.title('AWEInsh_2')
plt.plot(b)
plt.show()

f_index = None
AWEInsh = None
gc.collect()

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\NDWI.npy'
t = 'NDWI'
NDWI = np.load(folder)
f_index = hist1(NDWI, bins, t)
b = f_index[0][998:1003]
plt.title('NDWI_2')
plt.plot(b)
plt.show()

f_index = None
NDWI = None
gc.collect()

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\AWEIsh.npy'
t = 'AWEIsh'
AWEIsh = np.load(folder)
f_index = hist1(AWEIsh, bins, t)
print(f_index[0][318])
print(f_index[0][319])
print(f_index[0][530])
b = f_index[0][319:530]
plt.title('AWEIsh_2')
plt.plot(b)
plt.show()

f_index = None
AWEIsh = None
gc.collect()






