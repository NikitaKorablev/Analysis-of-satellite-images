import numpy as np
import tifffile
import matplotlib.pyplot as plt
import gc

def sres(band):
    print('index_corners: ', end = '')
    shape = band.shape
    mask = np.zeros(shape)

    np.putmask(mask,band!=band[0][0],1)

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
    
    print('complite')
    
    mask = None
    x_u_d = None
    y_l_r = None
    gc.collect()
    
    # Координаты точек:
    # print('x_up:    ', x_up)
    # print('x_down:  ', x_down)
    # print('y_left:  ', y_left)
    # print('y_right: ', y_right)    
    
    
    band = band[x_up:x_down]
    arr = [[0]*(y_left - y_right)]*band.shape[0]
    for i in range(band.shape[0]):
        arr[i] = band[i][(shape[1]-y_left):(shape[1]-y_right)]
    
    arr = np.array(arr)
    shape = None
    x_up = None
    x_down = None
    y_left = None
    y_right = None
    gc.collect()
    
    return arr

band = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/Landsat_B1.npy'
# image = tifffile.imread(band, key=0)
arr = np.load(band)

plt.figure(figsize=(20,10))
plt.title("AWEInsh.npy")
plt.imshow(arr, 'Greys')
plt.show()

print(arr.shape)

arr = sres(arr)

print(arr.shape)

plt.figure(figsize=(20,10))
plt.title("AWEInsh.npy")
plt.imshow(arr, 'Greys')
plt.show()









