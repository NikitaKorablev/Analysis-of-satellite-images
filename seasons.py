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

def bul_im(array, name):
    mask = np.zeros([array.shape[0], array.shape[1], 3], dtype=np.uint8)
    
    mask[array == 0] = [255, 255, 255]
    mask[array == 1] = [0, 0, 0]
    
    mask = Image.fromarray(mask)
    mask.save(os.getcwd() + '\\' + name + '.jpeg')
    
    mask = None
    gc.collect()

    

def TF(limit, f, name, name_save, file):
    bul = np.zeros([f.shape[0], f.shape[1]])
    bul_i = np.zeros([f.shape[0], f.shape[1]])
    bul_i[f == limit] = True
    bul_i[f != limit] = False
    
    np.putmask(bul, bul_i, 1)
    
    per = 100 * np.sum(bul)/(bul.shape[0] * bul.shape[1])
    
    print('sum = ', sum(bul.ravel()))
    # print(f_1.shape[0] * f_1.shape[1])
    # print(sum(bul.ravel())/(f_1.shape[0] * f_1.shape[1]))
    print('perсent of ' + name + ' = ', str(per)[:5])
    print()
    
    file.write('number of ' + name + 'cells: ' + str(np.sum(bul)) + '\n')
    file.write('perсent of ' + name + ' = ' + str(per)[:5] + '\n'*2)
    
    bul = None
    bul_i = None
    gc.collect()

def perсent(f_1, f_2, file, adres, first_index, second_index, name_save):
    f1 = np.zeros([f_1.shape[0], f_1.shape[1]])
    f2 = np.zeros([f_2.shape[0], f_2.shape[1]])
    f1[f_1 == 1] = 3 #water
    f1[f_1 == 0] = 1 #ground
    f2[f_2 == 1] = 15 #water
    f2[f_2 == 0] = 10 #ground
    f = f1 + f2
    
    mask = np.zeros([f_1.shape[0], f_1.shape[1], 3], dtype=np.uint8)
    
    # print("Текущая деректория:", os.getcwd())
    os.chdir('..')
    # print("Текущая деректория:", os.getcwd())
    
    if os.path.isdir('Statistics_of_seasons'):
        os.chdir('Statistics_of_seasons')
    
    year = str(adres.split('\\')[0])
    adres = adres.split('\\')[1]
    print(year)
    
    if not os.path.isdir(year):
        os.mkdir(year)
        
    os.chdir(year)
    
    if not os.path.isdir(adres):
        os.mkdir(adres)
        
    os.chdir(adres)
    
    name_file = first_index+'_'+second_index
    
    print("Текущая деректория:", os.getcwd())
    if not os.path.isdir(name_file):
        os.mkdir(name_file)
    
    os.chdir(name_file)
    
    # print("Текущая деректория:", os.getcwd())
    
    print('name_save: ', name_save)
    print('name_file: ', name_file)
    
    print()    
    
    name_save += '\\' + year + '\\' + adres + '\\' + name_file
    
    print(name_save + '\statistical_data_for_' + first_index + '_' + second_index + '.txt')
    file = open(name_save + '\statistical_data_for_' + first_index + '_' + second_index + '.txt', 'w+')
    
    name = 'water'
    limit = 18
    TF(limit, f, name, name_save, file)
    
    name = 'ground'
    limit = 11
    TF(limit, f, name, name_save, file)
    
    name = 'ground to water'
    limit = 16
    TF(limit, f, name, name_save, file)
    
    name = 'water to ground'
    limit = 13
    TF(limit, f, name, name_save, file)
    
    file.close()
    
    '---------------------------------------------------------'
    mask[f == 18] = [0, 0, 255]  # water                    blue
    mask[f == 11] = [150, 255, 0] # ground                  green
    
    mask[f == 16] = [255, 0, 0] # ground to water           red
    mask[f == 13] = [255, 90, 255] # water to ground        Pink
    
    
    # print("Текущая деректория:", os.getcwd())
    mask = Image.fromarray(mask)
    mask.save(os.getcwd() + '\mask_' + first_index + '_' + second_index + '.jpeg')
    
    mask = np.array(mask)

    plt.figure(figsize=(20,10))
    plt.title(name_file)
    plt.imshow(mask)
    plt.show()
    
    mask = None
    
    bul_im(f_1, 'bin_im_' + first_index)
    bul_im(f_2, 'bin_im_' + second_index)
    '---------------------------------------------------------'
    os.chdir('..')
    os.chdir('..')

# def door(adres):
#     print(adres)
#     k = []
#     if len(adres) == 2:
#         k = [1, 2]
#     elif len(adres) > 2:
#         print('Select the images you want to use (2 elements separating them with "enter"):', end='')
#         for i in range(0, 2):
#             k.append(int(input()))
#         k.sort()
#     if len(k) < 2:
#         print('!Chouse 3 elements!')
#         k = door()
#     return k


name_file = rt()

adres = glob.glob(name_file + r'\*\\')
# print('adres: ', adres)

name_file += '\\'

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
# print()

# k = door(adres)

# print(name_file)

# for i in range(0, len(adres)):
#     if adres[i].split('\\')[0] in name_file:
#         print(i, ' ', name_file, adres[i])
#         name_file = name_file[:name_file.find(adres[i].split('\\')[0])]
#         print(i, ' ', name_file, '\n')

# print('name_file: ', name_file)



def index_comparator(file, adres, names_of_indices, name_save):
    for first_index in names_of_indices:
        for second_index in names_of_indices:
            if first_index != second_index:
                f1 = np.load(file + adres.split('\\')[1] + '\mask_' + first_index + '.npy')
                # print(np.min(f1), np.max(f1))
                f2 = np.load(file + adres.split('\\')[1] + '\mask_' + second_index + '.npy')
                # print(np.min(f2), np.max(f2))
                
                perсent(f1, f2, file, adres, first_index, second_index, name_save)
                
                f1 = None
                f2 = None
                gc.collect



name_save = os.getcwd()[:os.getcwd().find('Scientific-work')] + 'Statistics_of_seasons'
print('name_save: ', name_save, '\n')


print('I started compearing!')
names_of_indices = ['NDWI', 'MNDWI', 'AWEI', 'MAWEI']
for i in adres:
    index_comparator(name_file, i, names_of_indices, name_save)





# season(rt())


# f1 = name_file + '\mask_MNDWI.npy'
# f2 = name_file + '\mask_NDWI.npy'
# f3 = name_file + '\mask_AWEInsh.npy'
# f4 = name_file + '\mask_AWEIsh.npy'


































