# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
from landsat_to_reflectance import l_to_r
from calc_indexes import getfun
from sres import sres
from rout import rout as rt
# from mask import mask

# # Адрес снимков
folder = rt()

# # Путь для сохранения
save = folder[:folder.find('LC08')]

# # Адрес MTL файла
lr_out = folder[:folder.find('_B')] + '_MTL.txt'

# # Адрес обрезанных снимков
lr_in = save + 'Band'

# # Адрес reflectance файлов
gf = save + 'Landsat_B'

# # Адрес канала для маски
# band = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/LC08_L1TP_175021_20180623_20180703_01_T1_B3.TIF'

print('----- Sres -----')
sres(folder, save)
print()
print('----- landsat_to_reflectance -----')
l_to_r(lr_in, lr_out, save) # пересчёт tiff в reflectance
print()
# mask(band)            # строим маску
print('----- Indices -----')
getfun(gf, save)        # считаем индексы с учётом маски


