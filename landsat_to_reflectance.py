import numpy as np
import tifffile


def l_to_r (folder, folder2):
    data = {}
    with open(folder2) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
            
    sun = float(data['SUN_ELEVATION'][1])
            
    for  i in range(9):
        print('Image №', i+1, ': ', end = '')
        image = tifffile.imread(folder + str(i+1)+'.tif', key=0)
        arr = np.array(image)
        Mult = float(data['REFLECTANCE_MULT_BAND_'+str(i+1)][1])
        Add = float(data['REFLECTANCE_ADD_BAND_'+str(i+1)][1])
        c = arr*Mult + Add
        s = c/np.sin(sun)
        band = np.array(s)
        np.save('Landsat_B' + str(i+1), band)
        print('complite')

 

