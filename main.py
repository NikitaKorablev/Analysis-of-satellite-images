# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
from landsat_to_reflectance import l_to_r
from calc_indexes import getfun
from sres import sres
# from mask import mask

# # Адрес снимков
# folder = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/LC08_L1TP_175021_20180623_20180703_01_T1_B'
folder = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/26-AUG/LC08_L1TP_175021_20180826_20180830_01_T1_B'


# # Адрес обрезанных снимков
lr_in = r'D:\NOU2020\Scientific-work\Band'

# # Адрес MTL файла
# lr_out = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_MTL.txt'
lr_out = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\26-AUG\LC08_L1TP_175021_20180826_20180830_01_T1_MTL.txt'

# Адрес reflectance файлов
gf = r'D:\NOU2020\Scientific-work\Landsat_B'

# Адрес канала для маски
# band = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/LC08_L1TP_175021_20180623_20180703_01_T1_B3.TIF'
print('----- Sres -----')
sres(folder)
print()
print('----- landsat_to_reflectance -----')
l_to_r(lr_in, lr_out) # пересчёт tiff в reflectance
print()
# mask(band)            # строим маску
print('----- Indices -----')
getfun(gf)        # считаем индексы с учётом маски




