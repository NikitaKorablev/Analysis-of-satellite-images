import numpy as np
import tifffile
import matplotlib.pyplot as plt
import gc

def sres(folder):    
    image = tifffile.imread(folder + str(1)+'.TIF', key=0)
    arr = np.array(image)

    # plt.figure(figsize=(20,10))
    # plt.title("Band" + str(j+1))
    # plt.imshow(arr, 'Greys')
    # plt.show()

    shape = arr.shape
    mask = np.zeros(shape)

    np.putmask(mask,arr!=arr[0][0],1)

    x_u_d = []  #x_up_down
    for y in range(shape[0]):
        if np.sum(mask[y,:])<=5 and np.sum(mask[y,:])!=0:
            for x in range(shape[1]):
                if mask[y][x] == 1:  
                    x_u_d.append(x)
                    break
    
    y_l_r = []  #y_left_right
    for x in range(shape[1]):
        if np.sum(mask[:,x])<=5 and np.sum(mask[:,x])!=0:
            for y in range(shape[0]):
                if mask[y][x] == 1:
                    y_l_r.append(y)
                    break
    
    y_left = max(y_l_r)
    y_right = min(y_l_r)
    x_up = min(x_u_d)
    x_down = max(x_u_d)
    
    image = None
    arr = None
    mask = None
    x_u_d = None
    y_l_r = None
    gc.collect()
    
    # Координаты точек:
    # print('x_up:    ', x_up)
    # print('x_down:  ', x_down)
    # print('y_left:  ', y_left)
    # print('y_right: ', y_right)
    
    for  j in range(9):
        if j+1 != 8:
            print('Image' + str(j+1) + ': ', end = '')
            image = tifffile.imread(folder + str(j+1)+'.TIF', key=0)
            arr = np.array(image)
            
            arr = arr[x_up:x_down]
            band = [[0]*(y_left - y_right)]*arr.shape[0]
            
            # print(type(arr))
            # print(type(band))
            
            for i in range(arr.shape[0]):
                band[i] = arr[i][(shape[1]-y_left):(shape[1]-y_right)]
            
            gc.collect()
            
            band = np.array(band)
            
            plt.figure(figsize=(20,10))
            plt.title("Band" + str(j+1))
            plt.imshow(band, 'Greys')
            plt.show()
            
            np.save("Band" + str(j+1), band)
            
            print('complite')
            
    shape = None
    x_up = None
    x_down = None
    y_left = None
    y_right = None
    gc.collect
    return

# folder = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/LC08_L1TP_175021_20180623_20180703_01_T1_B'

# arr = sres(folder)



