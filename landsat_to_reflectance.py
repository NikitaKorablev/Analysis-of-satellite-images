import numpy as np
import tifffile
X = '174022_20191009_20191018'

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_B'
folder2 = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_MTL.txt'
data={}

with open(folder2) as file:
    for line in file:
        key, *value = line.split()
        data[key] = value
 
sun = float(data['SUN_ELEVATION'][1])
        
for  i in range(7):
    image = tifffile.imread(folder + str(i+1)+'.tif', key=0)
    arr = np.array(image)
    Mult = float(data['REFLECTANCE_MULT_BAND_'+str(i+1)][1])
    Add = float(data['REFLECTANCE_ADD_BAND_'+str(i+1)][1])
    c = arr*Mult + Add
    s = c/np.sin(sun)
    band = np.array(s)
    np.save('Landsat_B' + str(i+1), band)