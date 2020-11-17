# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
from landsat_to_reflectance import l_to_r
from calc_indexes import getfun
from mask import mask

# Адрес снимков
lr_in = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_B'

# Адрес MTL файла
lr_out = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_MTL.txt'

# Адрес reflectance файлов
gf = r'D:\NOU2020\Scientific-work\Landsat_B'

# Адрес канала
band = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/LC08_L1TP_175021_20180623_20180703_01_T1_B3.TIF'


l_to_r(lr_in, lr_out) # пересчёт tiff в reflectdnce
mask(band)            # строим маску
f = getfun(gf)        # считаем индексы с учётом маски




