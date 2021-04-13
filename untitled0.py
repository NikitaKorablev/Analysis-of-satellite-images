# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:41:26 2021

@author: 1
"""

# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# array = np.zeros([100, 200, 3], dtype=np.uint8)
# array[:,:100] = [255, 128, 0] #Orange left side
# array[:,100:] = [0, 0, 255]   #Blue right side

# img = Image.fromarray(array)

# img = np.array(img)

# plt.imshow(img)
# plt.show()





# from rout import rout as rt

# name_date = rt()
# name_date = name_date[name_date.find('nnovgorod') + 10:name_date.find('\LC08')]

# s = '\ '
# for i in range(len(name_date)):
#     if name_date[i] == s[0]:
#         print(i)
#         name_date = name_date[:i] + '_' + name_date[i+1:]
# print(name_date)




# import os

# print("Текущая деректория:", os.getcwd())

# os.chdir('Статистика')
# print(os.getcwd())

# if not os.path.isdir("njnjn"):
#      os.mkdir("njnjn")
# print(os.getcwd())

# os.chdir('njnjn')
# print(os.getcwd())

# name_date = rt()
# name_date = name_date[name_date.find('nnovgorod') + 10:name_date.find('\LC08')]

# s = '\ '
# for i in range(len(name_date)):
#     if name_date[i] == s[0]:
#         name_date = name_date[:i] + '_' + name_date[i+1:]

# print("Текущая деректория:", os.getcwd())

# os.chdir('Статистика')

# if not os.path.isdir(name_date):
#      os.mkdir(name_date)

# print(os.getcwd())


# a = os.getcwd()
# print(a)
# if a.find('Статистика') == False:
#     os.chdir('Статистика')

# print(os.getcwd())


# IV = r'D:\other\tress_project\districts\sovetsky\sovetsky.shp'

# s = '\ '
# len_distr = len(IV.split(s[0])[-1])
# print(IV.split(s[0])[-1], len_distr)

# IV1 = IV[:-len_distr]
# print(IV1)


# from rout import rout as rt
# import glob

# name_file = rt()
# adres = name_file[:name_file.find('\LC08')]

# # adres = r'D:\NOU2020\EarthExplorer\nnovgorod\2018' + r'\*\\'
# year = glob.glob(adres)
# print(year, len(year))


# print(list(glob.glob('e:\\*\\')))


import numpy as np
import matplotlib.pyplot as plt
import tifffile
# from landsat_to_reflectance import l_to_r

# f1 = np.load(r'D:\NOU2020\EarthExplorer\nnovgorod\2018\22-MAY\mask_MNDWI.npy')

f2 = tifffile.imread(r'D:\NOU2020\EarthExplorer\nnovgorod\2016\28-JUL\LC08_L1TP_174021_20160728_20170322_01_T1_B5.TIF', key=0)
# f2 = tifffile.imread(r'D:\NOU2020\EarthExplorer\nnovgorod\2018\26-AUG\LC08_L1TP_175021_20180826_20180830_01_T1_B5.TIF', key=0)
# folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_'
# f2 = tifffile.imread(r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\LC08_L1TP_175021_20180623_20180703_01_T1_B5.TIF', key=0)
f2 = np.array(f2)

# f = np.load(r'D:\NOU2020\EarthExplorer\nnovgorod\2018\22-MAY\MNDWI.npy')


# for i in range(3000, 4001):
#     for j in range(3000, 4001):
#         f2[i][j] = 1000000



# f2 = np.array(f2)
# print(np.max(f2))

plt.figure(figsize=(20,10))
plt.title('f2')
plt.imshow(f2, 'Greys')
plt.show()

# save = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\23-JUN\\'
# lr_in = folder + 'B'
# lr_out = folder + 'MTL.txt'

# l_to_r(lr_in, lr_out, save) # пересчёт tiff в reflectance



# a = 'a'

# b = 'abia'

# for i in range(len(b)):
#     if a == b[i]:
#         del b[i]


# print(b)





































