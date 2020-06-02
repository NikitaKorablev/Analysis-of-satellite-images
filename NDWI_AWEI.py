from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt


def openFile(filepath):
    # Open the file:
    raster = gdal.Open(filepath) 
    band = raster.ReadAsArray()
    return band

folder = r'D:\EarthExplorer\NOU2020\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_B'

filepath_b3 = folder + '3.TIF'
filepath_b5 = folder + '5.TIF'
filepath_b9 = folder + '9.TIF'

b3 = openFile(filepath_b3)
b5 = openFile(filepath_b5)
b9 = openFile(filepath_b9)

#1 0.435–0.451 Coastal Aerosol (CA)
#2 0.452–0.512 Blue
#3 0.533–0.590 Green
#4 0.636–0.673 Red
#5 0.851–0.879 Near Infrared (NIR)
#6 1.566–1.651 Shortwave NIR 1 (SWIR1)
#7 2.107–2.294 Shortwave NIR 2 (SWIR2)

# NDWI = (Green − NIR)/(Green + NIR)
a = b3 - b5
b = b3 + b5
b[b == 0] = 1
NDWI = np.divide(a,b)
print (np.max(NDWI),' ',np.min(NDWI))
T = 0.3877
NDWI[NDWI >= T] = 1
NDWI[NDWI < T] = 0

NDWIwater = np.sum(NDWI)

plt.figure(figsize=(20,10))
plt.title("NDWI")
plt.imshow(NDWI,'Greys')
plt.show()

mindif = NDWI.shape[0] * NDWI.shape[1]
tmindif = 0

def normalize(array):
    array_min, array_max = array.min(), array.max()
    return ((array - array_min)/(array_max - array_min))

AWEI = 4*(b3-b5)-(0.25*b5+2.75*b9)
print (np.max(AWEI),' ',np.min(AWEI))
#T = 0.1897
#T = 0.189

qeuet = []
def podbor(A,step):
    lt = []
    for T in A:
        result = np.zeros(NDWI.shape)
        np.putmask(result, AWEI>=T, 1)
    
        AWEIwater = np.sum(result)
        D = abs(AWEIwater - NDWIwater)
#       print (T, ' ', D)
        lt.append((T,D,step))
    print('Non-equal pixels count: '+str(tmindif)+' '+str(mindif))
    lt.sort(key = lambda x: (x[1]))
    print (lt)
    return lt
    
step = 1000   
Tresholdes = np.arange(np.min(AWEI), np.max(AWEI), step)
dataT = podbor(Tresholdes,step)
qeuet = dataT[0:5]

mint = np.min(AWEI)
mindif = AWEI.shape[0]*AWEI.shape[1]


while(len(qeuet) > 0):
    dt = qeuet.pop()
    if (dt[1] < mindif):
        mindif = dt[1]
        mint = dt[0]
    if (dt[2] > 1):
        step = min(dt[2]//50, 1)
        data = np.arange(dt[0]-dt[2]//2, dt[0]+dt[2]//2, step)
        
        l = podbor(data,step)
        for i in range(min(5,len(data))):
            qeuet.append(l[i])

print (mint, ' ',mindif)






#file = open("D:/EarthExplorer/nnovgorod/2018/AWEI_2018.txt","a")
#file.write("23-JUN-2018:" + '\n')
#
#A = np.arange(tmindif-5, tmindif+5, 1)
#for T in A:
#    result = np.zeros(NDWI.shape)
#    np.putmask(result, AWEI>=T, 1)
#    
#    AWEIwater = np.sum(result)
#    D = abs(AWEIwater - NDWIwater)
#    B = str(T)+' '+str(D)
#
#    file.write(B + '\n')
#
#
#file.write('\n')
#file.close()


#    diff = AWEI - NDWI
#    diff[diff < 0] = 1
    
#    red = openFile(folder + '4.TIF')
#    green = b3
#    blue = openFile(folder + '2.TIF')
#    
#    red = normalize(red)
#    green = normalize(green)
#    blue = normalize(blue)
#    
#    plt.figure(figsize=(20,10))
#    plt.title("diff")
#    plt.imshow(diff)
#    plt.show()

#plt.figure(figsize=(20,10))
#plt.title("B5")
#plt.imshow(b5,'Greys')
#plt.show()

