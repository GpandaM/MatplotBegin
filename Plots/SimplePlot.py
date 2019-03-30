# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 22:45:01 2018

@author: Lenovo
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Data for plottig 
# t : time
# s : value
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
print(t)

fig, ax = plt.subplots()
ax.plot(t,s)

#ax.set(xlabel = 'time(s)', ylabel = 'volatge(mV)', title = "AS simple as you get folks")
#ax.grid()

fig.savefig("test1.png")
plt.show()
