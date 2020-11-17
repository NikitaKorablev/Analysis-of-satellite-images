import numpy as np
import tifffile
import gc

def mask (band):    
    image = tifffile.imread(band, key=0)
    arr = np.array(image)
    
    mask = np.array([[False]*arr.shape[1]]*arr.shape[0])
    
    print('mask editing:', end = '')
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (arr[i][j] == 0):
                mask[i][j] = True
    print('complite')
    
    image = None
    arr = None

    print('saving the mask: ', end = '')
    np.save('mask', mask)
    print('complite')
    
    mask = None
    gc.collect()
    
# band = r'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN/LC08_L1TP_175021_20180623_20180703_01_T1_B3.TIF'
# mask(band)

