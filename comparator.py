# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:52:48 2021

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
import gc
from rout import rout as rt
from PIL import Image


def TF(limit, f, name):
    bul = np.zeros([f_1.shape[0], f_1.shape[1]])
    bul_i = np.zeros([f_1.shape[0], f_1.shape[1]])
    bul_i[f == limit] = True
    bul_i[f != limit] = False
    
    np.putmask(bul, bul_i, 1)
    
    per = 100 * sum(bul.ravel())/(f_1.shape[0] * f_1.shape[1])
    
    print('sum = ', sum(bul.ravel()))
    # print(f_1.shape[0] * f_1.shape[1])
    # print(sum(bul.ravel())/(f_1.shape[0] * f_1.shape[1]))
    print('persent of ', name, '= ', str(per)[:5])
    print()
    
    bul = None
    bul_i = None
    gc.collect()


def persent(f_1, f_2, name_mask):
    f1 = np.zeros([f_1.shape[0], f_1.shape[1]])
    f2 = np.zeros([f_1.shape[0], f_1.shape[1]])
    f1[f_1 == 1] = 3 #water
    f1[f_1 == 0] = 1 #ground
    f2[f_2 == 1] = 15
    f2[f_2 == 0] = 10
    
    mask = np.zeros([f_1.shape[0], f_1.shape[1], 3], dtype=np.uint8)
    
    f = f1 + f2
    
    name = 'water'
    limit = max(f1.ravel()) + max(f2.ravel())
    TF(limit, f, name)
    
    name = 'ground'
    limit = min(f1.ravel()) + min(f2.ravel())
    TF(limit, f, name)
    
    name = 'ground and water'
    limit = min(f1.ravel()) + max(f2.ravel())
    TF(limit, f, name)
    
    name = 'water and ground'
    limit = max(f1.ravel()) + min(f2.ravel())
    TF(limit, f, name)
    
    
    '---------------------------------------------------------'
    mask[f == 18] = [0, 0, 255]  #water
    mask[f == 13] = [255, 90, 255] # ground
    mask[f == 16] = [255, 0, 0] # 1 picture - ground, 2 picture - water
    mask[f == 11] = [150, 255, 0] # 1 picture - water, 2 picture - ground
    
    mask = Image.fromarray(mask)
    mask = np.array(mask)
    
    plt.figure(figsize=(20,10))
    plt.title(name_mask)
    plt.imshow(mask)
    plt.show()
    
    # plt.figure(figsize=(20,10))
    # plt.title("mask_2")
    # plt.imshow(mask_2, 'Spectral')
    # plt.show()
    '---------------------------------------------------------'
    
    # f_r = f.ravel()
    # h = np.histogram(f_r, 100)
    
    # print(f_r.shape)
    
    # plt.title("gist")
    # plt.plot(h[0])
    # plt.show()






name = rt()
name = name[:name.find('\LC08')]

f1 = name + '\mask_MNDWI.npy'
f2 = name + '\mask_NDWI.npy'
f3 = name + '\mask_AWEInsh.npy'
f4 = name + '\mask_AWEIsh.npy'

f_1 = np.load(f1)
f_2 = np.load(f2)
f_3 = np.load(f3)
f_4 = np.load(f4)


name = 'MNDWI and NDWI'
print(name)
persent(f_1, f_2, name)

name = 'AWEInsh and AWEIsh'
print(name)
persent(f_3, f_4, name)

name = 'NDWI and AWEInsh'
print(name)
persent(f_2, f_3, name)

name = 'MNDWI and AWEIsh'
print(name)
persent(f_1, f_4, name)

































