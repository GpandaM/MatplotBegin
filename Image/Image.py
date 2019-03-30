# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 22:36:20 2018

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
#from PIL import Image

img1 = mpimg.imread("Bug.png")
print(img1)
imgplt = plt.imshow(img1)