# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:47:04 2020

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
import gc
from rout import rout as rt

def hist1 (index, bins, name):
    
    # plt.title(name + '_gist')
    
    f_index = index.ravel()
    # print('f_index.shape: ', f_index.shape)
    
    index = None
    gc.collect()
    
    h1 = np.histogram(f_index, bins)
    # print('shape: ', h1[0].shape)
    # plt.plot(h1[0])
    # plt.show()
    
    # print('h[0].shape: ', h1[0].shape)
    # print('h[1].shape: ', h1[1].shape)
    # print(type(h1))
    
    return h1
    
def hist2 (f, bins, name):
    
    result = np.zeros((bins))
    # print('f[0].shape: ', f[0].shape)
    for i in range(0, bins):
        result[i] = (sum(f[0][:i]))
    
    edges = np.array(f[1])
    # result[0] = result
    
    # plt.title(name)
    # plt.plot(result)
    # plt.show()
    
    return (result, edges)


def bin_ind(name):
    print(name)
    bins = 2000
    
    file = open(name + 'data_of_pixels.txt' , 'w+')
    
    
    '''  -----NDWI-----  '''
    print('\t', '  -----  NDWI  -----  ')
    p = 0.18
    folder = name + r'/NDWI.npy'
    t = 'NDWI'
    NDWI = np.load(folder)
    f_index_1 = hist1(NDWI, bins, t)
    
    plt.figure(figsize=(20,10))
    plt.title("NDWI")
    plt.imshow(NDWI, 'Greys')
    plt.show()
    
    f_index_2 = hist2(f_index_1, bins, t + '_stair')
    
    for i in range (0, bins):
        if f_index_2[1][i] >= p:
            break
    
    print('\t', 'water percent area: ', 100*(f_index_2[0][i])/(NDWI.shape[0]*NDWI.shape[1]))
    
    
    '''--------------------------------------------------------------------------------------------------'''
    mask = np.copy(NDWI)
    print(mask.shape)
    print(type(mask))
    
    mask[mask < p] = 0
    mask[mask >= p] = 1
    
    whater = np.sum(mask)
    ground = mask.shape[0]*mask.shape[1] - np.sum(mask)
    
    file.write('------' + t + '\n')
    file.write('whater count = ' + str(whater) + '\nground count = ' + str(ground) + '\n\n')
    
    plt.figure(figsize=(20,10))
    plt.title("mask_NDWI")
    plt.imshow(mask, 'Greys')
    plt.show()
    
    save = folder[:folder.find('NDWI')]
    np.save(save + "mask_NDWI", mask)
    '''--------------------------------------------------------------------------------------------------'''
    
    
    f_index_1 = None
    f_index_2 = None
    NDWI = None
    gc.collect()
    print()
    
    
    '''  -----MNDWI-----  '''
    print('\t', '  -----  MNDWI  -----  ')
    p = 0.18
    folder = name + '\MNDWI.npy'
    t = 'MNDWI'
    MNDWI = np.load(folder)
    f_index_1 = hist1(MNDWI, bins, t)
    
    plt.figure(figsize=(20,10))
    plt.title("MNDWI")
    plt.imshow(MNDWI, 'Greys')
    plt.show()
    
    f_index_2 = hist2(f_index_1, bins, t + '_stair')

    for i in range (0, bins):
        if f_index_2[1][i] >= p:
            break
    
    print('\t', 'water percent area: ', 100*(f_index_2[0][i])/(MNDWI.shape[0]*MNDWI.shape[1]))
    
    
    '''--------------------------------------------------------------------------------------------------'''
    mask = np.copy(MNDWI)
    print(mask.shape)
    print(type(mask))
    
    mask[mask < p] = 0
    mask[mask >= p] = 1
    
    whater = np.sum(mask)
    ground = mask.shape[0]*mask.shape[1] - np.sum(mask)
    
    file.write('------' + t + '\n')
    file.write('whater count = ' + str(whater) + '\nground count = ' + str(ground) + '\n\n')
    
    plt.figure(figsize=(20,10))
    plt.title("mask_MNDWI")
    plt.imshow(mask, 'Greys')
    plt.show()
    
    save = folder[:folder.find('MNDWI')]
    np.save(save + "mask_MNDWI", mask)
    '''--------------------------------------------------------------------------------------------------'''
    
    
    f_index_1 = None
    f_index_2 = None
    MNDWI = None
    gc.collect()
    print()
    
    
    
    
    '''  -----AWEInsh-----  '''
    print('\t', '  -----  AWEInsh  -----  ')
    p = 0.16
    folder = name + r'/AWEInsh.npy'
    t = 'AWEInsh'
    AWEInsh = np.load(folder)
    f_index_1 = hist1(AWEInsh, bins, t)
    
    plt.figure(figsize=(20,10))
    plt.title("AWEInsh")
    plt.imshow(AWEInsh, 'Greys')
    plt.show()

    f_index_2 = hist2(f_index_1, bins, t + '_stair')
    
    for i in range (0, bins):
        if f_index_2[1][i] >= p:
            break
    
    print('\t', 'water percent area: ', 100*(f_index_2[0][i])/(AWEInsh.shape[0]*AWEInsh.shape[1]))
    
    
    '''--------------------------------------------------------------------------------------------------'''
    mask = np.copy(AWEInsh)
    print(mask.shape)
    print(type(mask))
    
    mask[mask < p] = 0
    mask[mask >= p] = 1
    
    if np.sum(mask.ravel()) > (mask.shape[0]*mask.shape[1]/2):
        mask = 1 - mask
        
    whater = np.sum(mask)
    ground = mask.shape[0]*mask.shape[1] - np.sum(mask)
    
    file.write('------' + t + '\n')
    file.write('whater count = ' + str(whater) + '\nground count = ' + str(ground) + '\n\n')
    
    plt.figure(figsize=(20,10))
    plt.title("mask_AWEInsh")
    plt.imshow(mask, 'Greys')
    plt.show()
    
    save = folder[:folder.find('AWEInsh')]
    np.save(save + "mask_AWEInsh", mask)
    '''--------------------------------------------------------------------------------------------------'''
    
    
    f_index_1 = None
    f_index_2 = None
    AWEInsh = None
    gc.collect()
    print()
    
    
    
    '''  -----MAWEInsh-----  '''
    print('\t', '  -----  MAWEInsh  -----  ')
    p = 0.18
    folder = name + r'/MAWEInsh.npy'
    t = 'MAWEInsh'
    AWEInsh = np.load(folder)
    f_index_1 = hist1(AWEInsh, bins, t)
    
    plt.figure(figsize=(20,10))
    plt.title("MAWEInsh")
    plt.imshow(AWEInsh, 'Greys')
    plt.show()
    
    f_index_2 = hist2(f_index_1, bins, t + '_stair')
    
    for i in range (0, bins):
        if f_index_2[1][i] >= p:
            break
    
    print('\t', 'water percent area: ', 100*(f_index_2[0][i])/(AWEInsh.shape[0]*AWEInsh.shape[1]))
    
    
    '''--------------------------------------------------------------------------------------------------'''
    mask = np.copy(AWEInsh)
    print(mask.shape)
    print(type(mask))
    
    mask[mask < p] = 0
    mask[mask >= p] = 1
    
    if np.sum(mask.ravel()) > (mask.shape[0]*mask.shape[1]/2):
        mask = 1 - mask
    
    whater = np.sum(mask)
    ground = mask.shape[0]*mask.shape[1] - np.sum(mask)
    
    file.write('------' + t + '\n')
    file.write('whater count = ' + str(whater) + '\nground count = ' + str(ground) + '\n\n')
    
    plt.figure(figsize=(20,10))
    plt.title("mask_MAWEInsh")
    plt.imshow(mask, 'Greys')
    plt.show()
    
    save = folder[:folder.find('MAWEInsh')]
    np.save(save + "mask_MAWEInsh", mask)
    '''--------------------------------------------------------------------------------------------------'''
    
    
    f_index_1 = None
    f_index_2 = None
    AWEInsh = None
    gc.collect()
    print()
    
    
    
    
    file.close()
    






