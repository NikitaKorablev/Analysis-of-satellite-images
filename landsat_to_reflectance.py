import numpy as np


def l_to_r (folder, folder2):
    data = {}
    with open(folder2) as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
            
    sun = float(data['SUN_ELEVATION'][1])
            
    for  i in range(9):
        if i+1 != 8:
            print('Image №', i+1, ': ', end = '')
            arr = np.load(folder + str(i+1)+'.npy')
            Mult = float(data['REFLECTANCE_MULT_BAND_'+str(i+1)][1])
            Add = float(data['REFLECTANCE_ADD_BAND_'+str(i+1)][1])
            c = arr*Mult + Add
            s = c/np.sin(sun)
            band = np.array(s)
            np.save('Landsat_B' + str(i+1), band)
            print('complite')



