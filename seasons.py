# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:49:28 2021

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
import gc
from rout import rout as rt
from PIL import Image
import os
import glob

def TF(limit, f, name, name_save, file):
    bul = np.zeros([f_1.shape[0], f_1.shape[1]])
    bul_i = np.zeros([f_1.shape[0], f_1.shape[1]])
    bul_i[f == limit] = True
    bul_i[f != limit] = False
    
    np.putmask(bul, bul_i, 1)
    
    per = 100 * sum(bul.ravel())/(f_1.shape[0] * f_1.shape[1])
    
    print('sum = ', sum(bul.ravel()))
    # print(f_1.shape[0] * f_1.shape[1])
    # print(sum(bul.ravel())/(f_1.shape[0] * f_1.shape[1]))
    print('perсent of ' + name + ' = ', str(per)[:5])
    print()
    
    file.write('number of ' + name + 'cells: ' + str(sum(bul.ravel())) + '\n')
    file.write('perсent of ' + name + ' = ' + str(per)[:5] + '\n'*2)
    
    bul = None
    bul_i = None
    gc.collect()

def perсent(f_1, f_2, name_mask, name_save):
    f1 = np.zeros([f_1.shape[0], f_1.shape[1]])
    f2 = np.zeros([f_1.shape[0], f_1.shape[1]])
    f1[f_1 == 1] = 3 #water
    f1[f_1 == 0] = 1 #ground
    f2[f_2 == 1] = 15
    f2[f_2 == 0] = 10
    
    mask = np.zeros([f_1.shape[0], f_1.shape[1], 3], dtype=np.uint8)
    
    f = f1 + f2
    
    name_date = rt()
    name_date = name_date[name_date.find('nnovgorod') + 10:name_date.find('\LC08')]
    
    s = '\ '
    for i in range(len(name_date)):
        if name_date[i] == s[0]:
            name_date = name_date[:i] + '_' + name_date[i+1:]
    
    print("Текущая деректория:", os.getcwd())
    
    os.chdir('..')
    os.chdir('Статистика')
    
    if not os.path.isdir(name_date):
        os.mkdir(name_date)
    
    print("Текущая деректория:", os.getcwd())
    
    # print(os.getcwd() + s[0] + name_date + '\statistical_data_for_' + name_mask + '.txt')
    
    file = open(os.getcwd() + s[0] + name_date + '\statistical_data_for_' + name_mask + '.txt', 'w+')
    
    name = 'water'
    limit = 18
    TF(limit, f, name, name_save, file)
    
    name = 'ground'
    limit = 11
    TF(limit, f, name, name_save, file)
    
    name = 'ground and water'
    limit = 16
    TF(limit, f, name, name_save, file)
    
    name = 'water and ground'
    limit = 13
    TF(limit, f, name, name_save, file)
    
    file.close()
    
    '---------------------------------------------------------'
    mask[f == 18] = [0, 0, 255]  # water
    mask[f == 11] = [150, 255, 0] # ground
    mask[f == 16] = [255, 0, 0] # 1 picture - ground, 2 picture - water
    mask[f == 13] = [255, 90, 255] # 1 picture - water, 2 picture - ground
    
    mask = Image.fromarray(mask)
    mask.save(os.getcwd() + s[0] + name_date+ s[0] + name_mask + '.jpeg')
    
    mask = np.array(mask)
    
    plt.figure(figsize=(20,10))
    plt.title(name_mask)
    plt.imshow(mask)
    plt.show()
    '---------------------------------------------------------'


s = '\ '
adres = glob.glob(r'D:\NOU2020\EarthExplorer\nnovgorod\2015\*\\')
for i in range(0, len(adres)):
    a = adres[i].split('\\')
    if a[len(a)-1] == '':
        a = a[:(len(a)-1)]
    # print(a)
    # print(len(a))
    year_day_month =  a[len(a)-2] + s[0] + a[len(a)-1]
    adres[i] = year_day_month
    
print(adres)




# name_file = rt()
# name_file = name_file[:name_file.find('\LC08')]

# f1 = name_file + '\mask_MNDWI.npy'
# f2 = name_file + '\mask_NDWI.npy'
# f3 = name_file + '\mask_AWEInsh.npy'
# f4 = name_file + '\mask_AWEIsh.npy'

# f_1 = np.load(f1)  #MNDWI
# f_2 = np.load(f2)  #NDWI
# f_3 = np.load(f3)  #AWEInsh
# f_4 = np.load(f4)  #AWEIsh

# name_save = r'D:\NOU2020\Scientific-work\Статистика'
































