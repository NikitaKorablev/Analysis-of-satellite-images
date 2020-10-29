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
    print(f_index.shape)
    
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


# def obrez (f_index, bins):
#     s = 0
#     k = (sum(f_index)/100)*5
#     print(k)
#     for i in range(0, bins):   
#         s += f_index[i]
#         if s>= k:
#             print('i_min: ', i)
#             f_index = f_index[i:]
#             break
#     s = 0
#     print(s)
#     for i in range(0, bins, -1):
#         s += f_index[i]
#         print('i: ', i, ' s: ', s)
#         if s>= k:
#             print('i_max: ', i)
#             f_index = f_index[i:]
#             break
    
#     return f_index

bins = 2000

# folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\MNDWI.npy'
# t = 'MNDWI'
# MNDWI = np.load(folder)
# f_index_1 = hist1(MNDWI, bins, t)
# b = f_index_1[0][245:265]
# plt.title('MNDWI_2')
# plt.plot(b)
# plt.show()

# f_index = None
# MNDWI = None
# gc.collect()

# folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\AWEInsh.npy'
# t = 'AWEInsh'
# AWEInsh = np.load(folder)
# f_index_1 = hist1(AWEInsh, bins, t)
# b = f_index_1[0][203:310]
# plt.title('AWEInsh_2')
# plt.plot(b)
# plt.show()

# f_index = None
# AWEInsh = None
# gc.collect()

folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\NDWI.npy'
t = 'NDWI'
NDWI = np.load(folder)
f_index_1 = hist1(NDWI, bins, t)
# b = f_index_1[0][317:320]
# plt.title('NDWI_2')
# plt.plot(b)
# plt.show()

# print(f_index_1[1])
print(NDWI.min())


t = 'NDWI_stair'
f_index_2 = hist2(f_index_1, bins, t)

print('f_index_2[1]: ', f_index_2[1])

for i in range (0, bins):
    if f_index_2[1][i] >= 0.18:
        break

print('i: ', i)

print('f_index_2[0][i]: ', f_index_2[0][i])

print(100*(f_index_2[0][i])/(NDWI.shape[0]*NDWI.shape[1]))

f_index_1 = None
f_index_2 = None
NDWI = None
gc.collect()




folder = r'D:\NOU2020\EarthExplorer\nnovgorod\2018\11-SEP\AWEIsh.npy'
t = 'AWEIsh'
AWEIsh = np.load(folder)
f_index_1 = hist1(AWEIsh, bins, t)

plt.title("AWEIsh")
plt.imshow(AWEIsh, 'Greys')

b = f_index_1[0][317:320]
plt.title('AWEIsh_2')
plt.plot(b)
plt.show()

print(f_index_1[1])
print(AWEIsh.min())

t = 'AWEIsh_stair'
f_index_2 = hist2(f_index_1, bins, t)

print('f_index_2[1]: ', f_index_2[1])

for i in range (0, bins):
    if f_index_2[1][i] >= 0.16:
        break

print('i: ', i)

print('f_index_2[0][i]: ', f_index_2[0][i])

print(100*(f_index_2[0][i])/(AWEIsh.shape[0]*AWEIsh.shape[1]))


f_index_1 = None
f_index_2 = None
AWEIsh = None
gc.collect()






