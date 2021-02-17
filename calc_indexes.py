# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:36:11 2020

@author: 1
"""

import numpy as np
import gc


#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)


# b1 = np.load(folder + '1.npy')
# b2 = np.load(folder + '2.npy')
# b4 = np.load(folder + '4.npy')
# b5 = np.load(folder + '5.npy')
# b7 = np.load(folder + '7.npy')

def getfun (folder, save):
    # mask = np.load('D:/NOU2020/Scientific-work/mask.npy')
    """ MNDWI = (Blue − NIR)/(Blue + NIR) """
    print ("MNDWI:", end=' ')
    b2 = np.load(folder + '2.npy')
    b5 = np.load(folder + '5.npy')
    a = b2 - b5
    b = b2 + b5
    b[b == 0] = 1
    MNDWI = np.divide(a,b)
    # np.putmask(MNDWI, mask, 0)
    np.save(save + 'MNDWI', MNDWI)

    b2 = None
    b5 = None
    b = None
    MNDWI = None
    gc.collect()
    print ("complite")
    
    """ AWEInsh = 4*(Blue - Near) - (0.25*Red + 2.75*SWIR2) """
    print ("AWEInsh:", end=' ')
    b4 = np.load(folder + '4.npy')
    b7 = np.load(folder + '7.npy')
    c = 0.25*b4 + 2.75*b7
    AWEInsh = 4*a - c
    # np.putmask(AWEInsh, mask, 0)
    np.save(save + 'AWEInsh', AWEInsh)
    
    b4 = None
    b7 = None
    a = None
    c = None
    AWEInsh = None
    gc.collect()
    
    print ("complite")

    """ NDWI = (Blue − Red)/(Blue + Red) """
    print ("NDWI:", end=' ')
    b2 = np.load(folder + '2.npy')
    b4 = np.load(folder + '4.npy')
    a = b2 - b4
    b = b2 + b4
    b[b == 0] = 1
    NDWI = np.divide(a,b)
    # np.putmask(NDWI, mask, 0)
    np.save(save + 'NDWI', NDWI)
    
    b2 = None
    b4 = None
    a = None
    b = None
    NDWI = None
    gc.collect()
    
    print ("complite")

    """ AWEIsh = CA + 2.5*Blue - 1.5*(Red + Near) - 0.25*SWIR2 """
    print ("AWEIsh:", end=' ')
    b4 = np.load(folder + '4.npy')
    b5 = np.load(folder + '5.npy')
    a = b4 + b5
    
    b4 = None
    b5 = None
    gc.collect()
    
    b1 = np.load(folder + '1.npy')
    b2 = np.load(folder + '2.npy')
    b = b1 + 2.5*b2
    
    b1 = None
    b2 = None
    gc.collect()
    
    b7 = np.load(folder + '7.npy')
    
    AWEIsh = b - 1.5*a - 0.25*b7
    # np.putmask(AWEIsh, mask, 0)
    np.save(save + 'AWEIsh', AWEIsh)

    
    b7 = None
    a = None
    b = None
    AWEIsh = None
    gc.collect()

    print ("complite")








