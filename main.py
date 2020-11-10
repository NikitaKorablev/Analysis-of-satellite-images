# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
from landsat_to_reflectance import l_to_r
from calc_indexes import calcIndexes
from showIndexes import showNPY
from gistogram import hists


# lr_in = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\LC08_L1TP_175021_20180911_20180927_01_T1_B'
# lr_mtl = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\LC08_L1TP_175021_20180911_20180927_01_T1_MTL.txt'
# gf = r'D:\NOU2020\Scientific-work\Landsat_B'

lr_in = r'E:\GIS\LC08_L1TP_119041_20140807_20170420_01_T1\LC08_L1TP_119041_20140807_20170420_01_T1_B'
lr_mtl = r'E:\GIS\LC08_L1TP_119041_20140807_20170420_01_T1\LC08_L1TP_119041_20140807_20170420_01_T1_MTL.txt'
gf = r'E:\GIS\Water\Scientific-work\Landsat_B'
folder = r'E:\GIS\Water\Scientific-work'

# l_to_r(lr_in, lr_mtl)
# f = calcIndexes(gf)

# showNPY(folder)
hists(folder)


