# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
import numpy as np
# from landsat_to_reflectance import l_to_r
from calc_indexes import getfun


lr_in = r'D:\images_work\testlandsat\normal\LC08_L1TP_135018_20190704_20190718_01_T1.tar\LC08_L1TP_135018_20190704_20190718_01_T1_B'
lr_out = r'D:\images_work\testlandsat\normal\LC08_L1TP_135018_20190704_20190718_01_T1.tar\LC08_L1TP_135018_20190704_20190718_01_T1_MTL.txt'
gf = r'D:\NOU2020\EarthExplorer\nnovgorod\reflectance\Landsat_B'


# l_to_r(lr_in, lr_out)


f = getfun(gf)




