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
    
    """ NDWI = (Green − NIR)/(Green + NIR) """
    '''3, 5'''
    print ("NDWI:", end=' ')
    b5 = np.load(folder + '5.npy')
    b3 = np.load(folder + '3.npy')
    a = b3 - b5
    b = b3 + b5
    b[b == 0] = 1
    NDWI = np.divide(a,b)
    # np.putmask(NDWI, mask, 0)
    np.save(save + 'NDWI', NDWI)
    
    b5 = None
    b3 = None
    a = None
    b = None
    NDWI = None
    gc.collect()
    
    print ("complite")
    
    
    
    """ MNDWI = (Green − SWIR1)/(Green + SWIR1) """
    '''2, 5'''
    print ("MNDWI:", end=' ')
    b3 = np.load(folder + '3.npy')
    b6 = np.load(folder + '6.npy')
    a = b3 - b6
    b = b3 + b6
    b[b == 0] = 1
    MNDWI = np.divide(a,b)
    # np.putmask(MNDWI, mask, 0)
    np.save(save + 'MNDWI', MNDWI)
   
    print ("complite")
    
    a = None
    b = None
    b3 = None
    b6 = None
    MNDWI = None
    gc.collect()

    
    """ AWEI = 4*(Green − SWIR1) − (0.25*NIR + 2.75*SWIR1) """
    # '''4*(Blue - Near) - (0.25*Red + 2.75*SWIR2)'''
    
    '''3, 5, 6'''
    print ("AWEI:", end=' ')
    b3 = np.load(folder + '3.npy')
    b6 = np.load(folder + '6.npy')
    a = b3 - b6
    
    b5 = np.load(folder + '5.npy')
    b6 = np.load(folder + '6.npy')
    b = 0.25*b5 + 2.75*b6
    
    AWEI = 4*a - b
    # np.putmask(AWEInsh, mask, 0)
    np.save(save + 'AWEI', AWEI)
    
    print ("complite")
    
    a = None
    b = None
    # AWEInsh = None
    gc.collect()
    
    
    
    '''MAWEI = AWEI / (Green + NIR + SWIR1 + SWIR2)'''
    '3, 5, 6, 7'
    print ("MAWEI:", end=' ')
    
    b3 = np.load(folder + '3.npy')
    b5 = np.load(folder + '5.npy')
    b6 = np.load(folder + '6.npy')
    b7 = np.load(folder + '7.npy')
    a = b3 + b5 + b6 + b7
    
    a[a==0] = 1
    
    MAWEI = np.divide(AWEI, a)
    
    np.save(save + 'MAWEI', MAWEI)
    
    print ("complite")
    
    b3 = None
    b5 = None
    b6 = None
    b7 = None
    a = None
    AWEI = None
    MAWEI = None
    
    gc.collect()
    
    
    

    
    
    
    
    
    
    






