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
    '''2, 5'''
    print ("MNDWI:", end=' ')
    b2 = np.load(folder + '2.npy')
    b5 = np.load(folder + '5.npy')
    a = b2 - b5
    b = b2 + b5
    b[b == 0] = 1
    MNDWI = np.divide(a,b)
    # np.putmask(MNDWI, mask, 0)
    np.save(save + 'MNDWI', MNDWI)
   
    print ("complite")
    
    print('min_2: ', np.min(b2), 'max_2: ', np.max(b2))
    print('min_5: ', np.min(b5), 'max_5: ', np.max(b5))
    
    b2 = None
    b5 = None
    b = None
    MNDWI = None
    gc.collect()
    
    
    """ AWEInsh = 4*(Blue - Near) - (0.25*Red + 2.75*SWIR2) """
    '''4*(Green − SWIR1) − (0.25*NIR + 2.75*SWIR1)'''
    
    '''2, 4, 5, 7'''
    print ("AWEInsh:", end=' ')
    # b3 = np.load(folder + '3.npy')
    b4 = np.load(folder + '4.npy')
    # b5 = np.load(folder + '5.npy')
    # b6 = np.load(folder + '6.npy')
    b7 = np.load(folder + '7.npy')
    
    # a = 4*(b3 - b6)
    # c = 0.25*b5 + 2.75*b6
    
    # AWEInsh = a - c
    
    
    c = 0.25*b4 + 2.75*b7
    AWEInsh = 4*a - c
    # np.putmask(AWEInsh, mask, 0)
    np.save(save + 'AWEInsh', AWEInsh)
    
    print ("complite")
    
    # print('min_4: ', np.min(b4), 'max_4: ', np.max(b4))
    # print('min_7: ', np.min(b7), 'max_7: ', np.max(b7))
    
    b4 = None
    b7 = None
    a = None
    c = None
    AWEInsh = None
    gc.collect()
    
    

    """ NDWI = (Nir − Red)/(Nir + Red) """
    '''4, 5'''
    print ("NDWI:", end=' ')
    b5 = np.load(folder + '5.npy')
    b4 = np.load(folder + '4.npy')
    a = b4 - b5
    b = b4 + b5
    b[b == 0] = 1
    NDWI = np.divide(a,b)
    # np.putmask(NDWI, mask, 0)
    np.save(save + 'NDWI', NDWI)
    
    b5 = None
    b4 = None
    a = None
    b = None
    NDWI = None
    gc.collect()
    
    print ("complite")

    """ AWEIsh = CA + 2.5*Blue - 1.5*(Red + NIR) - 0.25*SWIR2 """
    '''AWEIsh = Blue + 2.5*Green - 1.5*(NIR + SWIR1) - 0.25*SWIR2'''
    
    '''1, 2, 4, 5, 7'''
    print ("AWEIsh:", 'end=' '')
    # b4 = np.load(folder + '4.npy')
    b5 = np.load(folder + '5.npy')
    b6 = np.load(folder + '6.npy')
   
    # a = 1.5*(b4 + b5)
    a = 1.5*(b5 + b6)
    
    # b4_max = np.max(b4)
    # b5_max = np.max(b5)
    # a_max = b4_max + b5_max
    # print('a_max = ', a_max)
    
    b4 = None
    b5 = None
    gc.collect()
    
    # b1 = np.load(folder + '1.npy')
    b2 = np.load(folder + '2.npy')
    b3 = np.load(folder + '3.npy')
    # b = b1 + 2.5*b2
    b = b2 + 2.5*b3
    
    
    # b1_max = np.max(b1)
    # b2_max = np.max(b2)
    # print('b2_max = ', b2_max)
    # b_max = b1_max + 2.5*b2_max
    # print('b_max = ', b_max)


    b2 = None
    gc.collect()
    
    b7 = np.load(folder + '7.npy')
    
    AWEIsh = b - a - 0.25*b7
    # np.putmask(AWEIsh, mask, 0)
    np.save(save + 'AWEIsh', AWEIsh)

    
    b7 = None
    a = None
    b = None
    AWEIsh = None
    gc.collect()

    # print ("complite")

    # print('min_1: ', np.min(b1), 'max_1: ', np.max(b1))

    b1 = None
    gc.collect()





