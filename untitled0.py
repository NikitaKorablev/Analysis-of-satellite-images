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





from rout import rout as rt

# name_date = rt()
# name_date = name_date[name_date.find('nnovgorod') + 10:name_date.find('\LC08')]

# s = '\ '
# for i in range(len(name_date)):
#     if name_date[i] == s[0]:
#         print(i)
#         name_date = name_date[:i] + '_' + name_date[i+1:]
# print(name_date)




import os

# print("Текущая деректория:", os.getcwd())

# os.chdir('Статистика')
# print(os.getcwd())

# if not os.path.isdir("njnjn"):
#      os.mkdir("njnjn")
# print(os.getcwd())

# os.chdir('njnjn')
# print(os.getcwd())

name_date = rt()
name_date = name_date[name_date.find('nnovgorod') + 10:name_date.find('\LC08')]

# s = '\ '
# for i in range(len(name_date)):
#     if name_date[i] == s[0]:
#         name_date = name_date[:i] + '_' + name_date[i+1:]

# print("Текущая деректория:", os.getcwd())

# os.chdir('Статистика')

# if not os.path.isdir(name_date):
#      os.mkdir(name_date)

# print(os.getcwd())


a = os.getcwd()
print(a)
if a.find('Статистика') == False:
    os.chdir('Статистика')

print(os.getcwd())

















