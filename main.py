# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:00:09 2020

@author: 1
"""
from landsat_to_reflectance import l_to_r
from calc_indices import getfun
from sres import sres
from sres_coordinate import sres_cd as sr_cd
from rout import rout as rt
from coordinate import coordinate as cd
from gist_bin import bin_ind
import glob
# from mask import mask

def main(folder, adres):
    # # Путь для сохранения
    # save = folder[:folder.find('LC08')]
    save = adres
    # print('save', save)
    # print('adres', adres)
    
    # # Адрес MTL файла
    # print('type_folder:', type(folder))
    # print('folder:', folder)
    lr_out = folder[:folder.find('_B')] + '_MTL.txt'
    # print('lr_out', lr_out)
    
    # # Адрес обрезанных снимков
    lr_in = save + 'Band'
    # lr_in = folder
    
    # # Адрес reflectance файлов
    gf = save + 'Landsat_B'
    
    a = 56.334723
    b = 43.977427
    y, x = cd(folder, b, a)
    
    print('----- Sres -----')
    # sres(folder, save)
    sr_cd(folder[:folder.find('1.TIF')], save, y, x)
    print()
    
    print('----- landsat_to_reflectance -----')
    l_to_r(lr_in, lr_out, save) # пересчёт tiff в reflectance
    print()
    
    print('----- Indices -----')
    getfun(gf, save)        # считаем индексы с учётом маски
    print()



# # Адрес снимков
folder = rt() + '\*\\'
adres = glob.glob(folder)
# print('adres', adres, '\n')

print('What would you like to do:\n1. main prog \n2. calc indices with limit\n3. do everithing')

a = input()
if a == '1':
    print('You chosed: <<main prog>>')
    for i in range(len(adres)):
        folder = glob.glob(adres[i] + '*.TIF')
        # print(folder, '\n')
        for j in range(0, len(folder)):
            if 'B1' in folder[j]:
                folder = folder[j]
                break
        # print('folder', folder, '\n')
        main(folder, adres[i])
            
elif a == '2':
    print('You choused: <<calc indices with limit>>')
    for i in range(len(adres)):
        folder = glob.glob(adres[i] + '*.TIF')
        # print(folder, '\n')
        for j in range(0, len(folder)):
            if 'B1' in folder[j]:
                folder = folder[j]
                break
        # print(folder, '\n')
        bin_ind(adres[i])

elif a == '':
    print('You choused: <<Do everithing>>')
    for i in range(len(adres)):
        # print(adres)
        folder = glob.glob(adres[i] + '*.TIF')
        # print(folder, '\n')
        for j in range(0, len(folder)):
            if 'B1' in folder[j]:
                folder = folder[j]
                break
        print(folder, '\n')
        
        print('------------ main prog ------------\n')
        
        main(folder, adres[i])
        
        print('---- calc indices with limit ----\n')
        # print(adres)
        bin_ind(adres[i])
        print('\n\n\n')

    
    
        







