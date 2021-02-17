# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:41:26 2021

@author: 1
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

array = np.zeros([100, 200, 3], dtype=np.uint8)
array[:,:100] = [255, 128, 0] #Orange left side
array[:,100:] = [0, 0, 255]   #Blue right side

img = Image.fromarray(array)

img = np.array(img)

plt.imshow(img)
plt.show()




