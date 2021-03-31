# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:08:37 2021

@author: 1
"""
import numpy as np
import tifffile
import matplotlib.pyplot as plt
import gc

# folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\22-MAY\LC08_L1TP_175021_20180522_20180605_01_T1_B'
# save = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\22-MAY\\'

def sres_cd(folder, save, y, x):
    for j in range(9):
        if j+1 != 8:
            print('Image' + str(j+1) + ': ', end = '')
            image = tifffile.imread(folder + str(j+1)+'.TIF', key=0)
            arr = np.array(image)
            
            # shape = arr.shape
            # x = 6859
            # y = 2603
            
            x_left = x - 600
            x_right = x + 400
            
            y_up = y - 400
            y_down = y + 600
            
            arr = arr[y_up:y_down]
            band = [[0]*(x_right - x_left)]*arr.shape[0]
            
            # print(type(arr))
            # print(type(band))
            
            for i in range(arr.shape[0]):
                band[i] = arr[i][(x_left):(x_right)]
            
            gc.collect()
            
            band = np.array(band)
            
            plt.figure(figsize=(20,10))
            plt.title("Band" + str(j+1))
            plt.imshow(band, 'Greys')
            plt.show()
            
            np.save(save + "Band" + str(j+1), band)
            
            print('complite')

# sres_cd(folder, save, 2603, 6859)











