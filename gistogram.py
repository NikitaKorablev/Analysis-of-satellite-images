# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:47:04 2020

@author: 1
"""

import numpy as np
import matplotlib.pyplot as plt
import gc

def hist1 (index, bins, name):
    
    plt.title(name + '_gist')
    
    f_index = index.ravel()
    print('f_index.shape: ', f_index.shape)
    
    index = None
    gc.collect()
    
    h1 = np.histogram(f_index, bins)
    print('shape: ', h1[0].shape)
    plt.plot(h1[0])
    plt.show()
    
    print('h[0].shape: ', h1[0].shape)
    print('h[1].shape: ', h1[1].shape)
    print(type(h1))
    
    return h1
    
def hist2 (f, bins, name):
    
    result = np.zeros((bins))
    print('f[0].shape: ', f[0].shape)
    for i in range(0, bins):
        result[i] = (sum(f[0][:i]))
    
    edges = np.array(f[1])
    # result[0] = result
    
    plt.title(name)
    plt.plot(result)
    plt.show()
    
    return (result, edges)


bins = 2000

# name = 'D:/NOU2020/EarthExplorer/nnovgorod/2018/23-JUN'
# name = 'D:/NOU2020/EarthExplorer/nnovgorod/2018/26-AUG'
name = 'D:/NOU2020/EarthExplorer/nnovgorod/2019/13-AUG'


'''  -----MNDWI-----  '''
print('  -----  MNDWI  -----  ')
folder = name + r'/MNDWI.npy'
t = 'MNDWI'
MNDWI = np.load(folder)
f_index_1 = hist1(MNDWI, bins, t)

plt.figure(figsize=(20,10))
plt.title("MNDWI")
plt.imshow(MNDWI, 'Greys')
plt.show()

# b = f_index_1[0][245:265]
# plt.title('MNDWI_2')
# plt.plot(b)
# plt.show()

print('MNDWI.min(): ', MNDWI.min())

t = 'MNDWI_stair'
f_index_2 = hist2(f_index_1, bins, t)

print('f_index_2[1]: ', f_index_2[1])

for i in range (0, bins):
    if f_index_2[1][i] >= 0.18:
        break

print('i: ', i)

print('f_index_2[0][i]: ', f_index_2[0][i])

print('water percent area: ', 100*(f_index_2[0][i])/(MNDWI.shape[0]*MNDWI.shape[1]))

f_index_1 = None
f_index_2 = None
MNDWI = None
gc.collect()
print()



'''  -----AWEInsh-----  '''
print('  -----  AWEInsh  -----  ')
folder = name + r'/AWEInsh.npy'
t = 'AWEInsh'
AWEInsh = np.load(folder)
f_index_1 = hist1(AWEInsh, bins, t)

plt.figure(figsize=(20,10))
plt.title("AWEInsh")
plt.imshow(AWEInsh, 'Greys')
plt.show()

# b = f_index_1[0][203:310]
# plt.title('AWEInsh_2')
# plt.plot(b)
# plt.show()

print('AWEInsh.min(): ', AWEInsh.min())

t = 'AWEInsh_stair'
f_index_2 = hist2(f_index_1, bins, t)

print('f_index_2[1]: ', f_index_2[1])

for i in range (0, bins):
    if f_index_2[1][i] >= 0.16:
        break

print('i: ', i)

print('f_index_2[0][i]: ', f_index_2[0][i])

print('water percent area: ', 100*(f_index_2[0][i])/(AWEInsh.shape[0]*AWEInsh.shape[1]))

f_index_1 = None
f_index_2 = None
AWEInsh = None
gc.collect()
print()



'''  -----NDWI-----  '''
print('  -----  NDWI  -----  ')
folder = name + r'/NDWI.npy'
t = 'NDWI'
NDWI = np.load(folder)
f_index_1 = hist1(NDWI, bins, t)

plt.figure(figsize=(20,10))
plt.title("NDWI")
plt.imshow(NDWI, 'Greys')
plt.show()

# b = f_index_1[0][317:320]
# plt.title('NDWI_2')
# plt.plot(b)
# plt.show()

# print(f_index_1[1])
print('NDWI.min(): ', NDWI.min())

t = 'NDWI_stair'
f_index_2 = hist2(f_index_1, bins, t)

print('f_index_2[1]: ', f_index_2[1])

for i in range (0, bins):
    if f_index_2[1][i] >= 0.18:
        break

print('i: ', i)

print('f_index_2[0][i]: ', f_index_2[0][i])

print('water percent area: ', 100*(f_index_2[0][i])/(NDWI.shape[0]*NDWI.shape[1]))

f_index_1 = None
f_index_2 = None
NDWI = None
gc.collect()
print()



'''  -----AWEIsh-----  '''
print('  -----  AWEIsh  -----  ')
folder = name + r'/AWEIsh.npy'
t = 'AWEIsh'
AWEIsh = np.load(folder)
f_index_1 = hist1(AWEIsh, bins, t)

plt.figure(figsize=(20,10))
plt.title("AWEIsh")
plt.imshow(AWEIsh, 'Greys')
plt.show()

# b = f_index_1[0][317:320]
# plt.title('AWEIsh_2')
# plt.plot(b)
# plt.show()

# print(f_index_1[1])
print('AWEIsh.min(): ', AWEIsh.min())

t = 'AWEIsh_stair'
f_index_2 = hist2(f_index_1, bins, t)

print('f_index_2[1]: ', f_index_2[1])

for i in range (0, bins):
    if f_index_2[1][i] >= 0.16:
        break

print('i: ', i)

print('f_index_2[0][i]: ', f_index_2[0][i])

print('water percent area: ', 100*(f_index_2[0][i])/(AWEIsh.shape[0]*AWEIsh.shape[1]))


f_index_1 = None
f_index_2 = None
AWEIsh = None
gc.collect()






