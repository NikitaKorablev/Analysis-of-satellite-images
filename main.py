# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
from landsat_to_reflectance import l_to_r
from calc_indexes import getfun


lr_in = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\LC08_L1TP_175021_20180911_20180927_01_T1_B'
lr_out = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\LC08_L1TP_175021_20180911_20180927_01_T1_MTL.txt'
gf = r'D:\NOU2020\Scientific-work\Landsat_B'


l_to_r(lr_in, lr_out)


f = getfun(gf)




