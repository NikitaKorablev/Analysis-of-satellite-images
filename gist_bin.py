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
    
    
    
    
    '''  -----AWEI-----  '''
    print('\t', '  -----  AWEI  -----  ')
    p = 0.16
    folder = name + r'/AWEI.npy'
    t = 'AWEI'
    AWEI = np.load(folder)
    f_index_1 = hist1(AWEI, bins, t)
    
    plt.figure(figsize=(20,10))
    plt.title("AWEI")
    plt.imshow(AWEI, 'Greys')
    plt.show()

    f_index_2 = hist2(f_index_1, bins, t + '_stair')
    
    for i in range (0, bins):
        if f_index_2[1][i] >= p:
            break
    
    print('\t', 'water percent area: ', 100*(f_index_2[0][i])/(AWEI.shape[0]*AWEI.shape[1]))
    
    
    '''--------------------------------------------------------------------------------------------------'''
    mask = np.copy(AWEI)
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
    plt.title("mask_AWEI")
    plt.imshow(mask, 'Greys')
    plt.show()
    
    save = folder[:folder.find('AWEI')]
    np.save(save + "mask_AWEI", mask)
    '''--------------------------------------------------------------------------------------------------'''
    
    
    f_index_1 = None
    f_index_2 = None
    AWEI = None
    gc.collect()
    print()
    
    
    
    '''  -----MAWEI-----  '''
    print('\t', '  -----  MAWEI  -----  ')
    p = 0.18
    folder = name + r'/MAWEI.npy'
    t = 'MAWEI'
    MAWEI = np.load(folder)
    f_index_1 = hist1(MAWEI, bins, t)
    
    plt.figure(figsize=(20,10))
    plt.title("MAWEI")
    plt.imshow(MAWEI, 'Greys')
    plt.show()
    
    f_index_2 = hist2(f_index_1, bins, t + '_stair')
    
    for i in range (0, bins):
        if f_index_2[1][i] >= p:
            break
    
    print('\t', 'water percent area: ', 100*(f_index_2[0][i])/(MAWEI.shape[0]*MAWEI.shape[1]))
    
    
    '''--------------------------------------------------------------------------------------------------'''
    mask = np.copy(MAWEI)
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
    plt.title("mask_MAWEI")
    plt.imshow(mask, 'Greys')
    plt.show()
    
    save = folder[:folder.find('MAWEI')]
    np.save(save + "mask_MAWEI", mask)
    '''--------------------------------------------------------------------------------------------------'''
    
    
    f_index_1 = None
    f_index_2 = None
    MAWEI = None
    gc.collect()
    print()
    
    file.close()
    






