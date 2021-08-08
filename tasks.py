#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Usman Naz
"""

#%%
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#%% Script 1: using NumPy to use slicing to put back image a and b together
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')

row_to_center_for_a = 297
col_to_center_for_a = 250
row_to_center_for_b = 160
col_to_center_for_b = 120

row_start = row_to_center_for_a - row_to_center_for_b
row_end = row_to_center_for_a + row_to_center_for_b
col_start = col_to_center_for_a - col_to_center_for_b
col_end = col_to_center_for_a + col_to_center_for_b

c = np.copy(a)
c[row_start:row_end, col_start:col_end, :] = b

mpimg.imsave('c.jpg', c)

#%% Script 2: using NumPy to reveal differences between 2 images
d = mpimg.imread('d.jpg')
e = mpimg.imread('e.jpg')

d_copy = np.copy(d)
e_copy = np.copy(e)

# convert datatypes to float to avoid int overflow
d_copy = d_copy.astype(np.float32)
e_copy = e_copy.astype(np.float32)

# convert negative values to positive
f = d_copy - e_copy
for r in range(f.shape[0]):
    for s in range(f.shape[1]): 
        for t in range(f.shape[2]):
            if f[r][s][t] < 0:
                f[r][s][t] = f[r][s][t] * -1.0
# covert datatype of final image back to int
f = f.astype(np.uint8)

mpimg.imsave('f.jpg', f)

#%% Script 3: using NumPy to place minion in another img to change its background
minion = mpimg.imread('g.jpg')
shugga = mpimg.imread('h.jpg')

img = np.copy(minion)
r, g, b = img[..., 0], img[..., 1], img[..., 2]
# gets all pixels in minion img that are not the minion (i.e. the background)
get_minion = np.logical_not((r < 200) & (g <= 255) & (g >= 220) & (b < 125))

# get position of where to place minion in shugga image
row_start = 1137
row_end = 1667
col_start = 920
col_end = 1580

# apply mask from minion to shugga image
i = np.copy(shugga)
mask = get_minion
i[row_start:row_end, col_start:col_end][mask] = img[mask]

mpimg.imsave('i.jpg', i)