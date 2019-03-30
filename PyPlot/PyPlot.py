# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:05:02 2018

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np

a = plt.figure("Fig:1")
plt.plot([1,2,3,4])
plt.ylabel("Given data")
plt.xlabel("X axis will be get adjusted according to the y label data")
plt.title("ONLY y-axis data is given", loc = 'left')
a.show()


b = plt.figure("Fig:2")
plt.subplot(212)
plt.plot([1,2,3,4], [10,20,30,40], 'ro')
#plt.axis(1, 5, 5, 50)
plt.title("X and Y axis Data is given" , loc = 'center')
b.show()


c = plt.figure("Fig:3")
plt.subplot(211)
t = np.arange(0, 5, 0.15)
c1 = plt.plot(t, t, 'ro' , t, t*t, 'b-', t, t**3, 'gs')
plt.setp(c1, linewidth = 8.0)
print(type(c1))
plt.show()




input()  #To keep the figure alive