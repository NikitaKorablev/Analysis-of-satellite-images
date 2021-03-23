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
    bul = np.zeros([f.shape[0], f.shape[1]])
    bul_i = np.zeros([f.shape[0], f.shape[1]])
    bul_i[f == limit] = True
    bul_i[f != limit] = False
    
    np.putmask(bul, bul_i, 1)
    
    per = 100 * sum(bul.ravel())/(f.shape[0] * f.shape[1])
    
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

def perсent(f_1, f_2, f_3, name_file, name_indices, name_save):
    f1 = np.zeros([f_1.shape[0], f_1.shape[1]])
    f2 = np.zeros([f_2.shape[0], f_2.shape[1]])
    f3 = np.zeros([f_3.shape[0], f_3.shape[1]])
    f1[f_1 == 0] = 2 #ground
    f1[f_1 == 1] = 0 #water
    f2[f_2 == 0] = 13 #ground
    f2[f_2 == 1] = 10 #water
    f3[f_3 == 0] = 33 #ground
    f3[f_3 == 1] = 20 #water
    f = f1 + f2 + f3
    
    mask = np.zeros([f_1.shape[0], f_1.shape[1], 3], dtype=np.uint8)
    
    file = open(name_save + '\\' + name_file + '\statistical_data_for_' + name_indices + '.txt', 'w+')
    
    name = 'water'
    limit = 0 + 10 + 20 #30
    TF(limit, f, name, name_save, file)
    
    name = 'ground'
    limit = 2 + 13 + 33 #48
    TF(limit, f, name, name_save, file)
    
    name = 'ground ground water'
    limit = 2 + 13 + 20 #35
    TF(limit, f, name, name_save, file)
    
    name = 'ground water ground'
    limit = 2 + 10 + 33 #45
    TF(limit, f, name, name_save, file)
    
    name = 'ground water water'
    limit = 2 + 10 + 20 #32
    TF(limit, f, name, name_save, file)
    
    name = 'water ground ground'
    limit = 0 + 13 + 33 #46
    TF(limit, f, name, name_save, file)
    
    name = 'water ground water'
    limit = 0 + 13 + 20 #33
    TF(limit, f, name, name_save, file)
    
    name = 'water water ground'
    limit = 0 + 10 + 33 #43
    TF(limit, f, name, name_save, file)
    
    file.close()
    
    '---------------------------------------------------------'
    mask[f == 30] = [0, 0, 255]  # water
    mask[f == 48] = [150, 255, 0] # ground
    
    mask[f == 35] = [255, 0, 0] # ground ground water
    mask[f == 45] = [255, 90, 255] # ground water ground
    
    mask[f == 32] = [255, 0, 0] # ground water water
    mask[f == 46] = [255, 90, 255] # water ground ground
    
    mask[f == 33] = [255, 0, 0] # water ground water
    mask[f == 43] = [255, 90, 255] # water water ground
    
    
    
    mask = Image.fromarray(mask)
    # mask.save(os.getcwd() + s[0] + name_date+ s[0] + name_file + '.jpeg')
    
    mask = np.array(mask)
    
    plt.figure(figsize=(20,10))
    plt.title(name_image)
    plt.imshow(mask)
    plt.show()
    '---------------------------------------------------------'



name_file = rt()
a = name_file.split('\\')
adres = name_file[:name_file.find(a[len(a)-2])] + r'\*\\'

adres = glob.glob(adres)
# print(adres)

for i in range(0, len(adres)):
    a = adres[i].split('\\')
    if a[len(a)-1] == '':
        a = a[:(len(a)-1)]
    # print(a)
    # print(len(a))
    year_day_month =  a[len(a)-2] + '\\' + a[len(a)-1]
    adres[i] = year_day_month

a = None
print(adres)
print()

def door():
    if len(adres) == 3:
        k = [1, 2, 3]
    elif len(adres) > 3:
        print('Select the images you want to use (3 elements separating them with "enter"):', end='')
        k = []
        for i in range(0, 3):
            k.append(int(input()))
        k.sort()
    if len(k) < 3:
        print('!Chouse 3 elements!')
        k = door()
    return k

k = door()

for i in range(0, len(adres)):
    if adres[i] in name_file:
        name_file = name_file[:name_file.find(adres[i])]

# print(name_file)

'''-----------------ПЕРЕПИСАТЬ В ФУНКЦИЮ------------------'''
name_indices = 'MNDWI'
f = []
for i in range(0, 3):
    f.append(name_file + adres[k[i]-1] + '\mask_' + name_indices + '.npy')
# print(f)

f1 = np.load(f[0])
print(np.min(f1), np.max(f1))
f2 = np.load(f[1])
print(np.min(f2), np.max(f2))
f3 = np.load(f[2])
print(np.min(f3), np.max(f3))

f = None
gc.collect()

name_save = os.getcwd()[:os.getcwd().find('Scientific-work')] + 'Statistics_of_seasons'
print('name_save: ', name_save)

for i in range(0, len(adres)):
    a = adres[i].split('\\')
    adres[i] = a[1]

year = int(a[0])
name_image = adres[k[0]-1] + '_' + adres[k[1]-1] + '_' + adres[k[2]-1] + '_'+ str(year)
print('name_image :', name_image)
perсent(f1, f2, f3, name_image, name_indices, name_save)







# f1 = name_file + '\mask_MNDWI.npy'
# f2 = name_file + '\mask_NDWI.npy'
# f3 = name_file + '\mask_AWEInsh.npy'
# f4 = name_file + '\mask_AWEIsh.npy'


































