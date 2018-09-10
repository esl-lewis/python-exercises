# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:03:44 2018

@author: fhs33517
"""

import random as rnd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt



xp = 0 
yp = 0
#initial particle position

n = 1000
#number of steps
steps = 0

#here is list to be plotted
xdata = []
ydata = []

for steps in range(n):
    x = rnd.randint(1,4)
    if x == 4:
        xp = xp + 1
        xdata.append(xp)
        ydata.append(yp)
    if x == 2:
        xp = xp - 1
        xdata.append(xp)
        ydata.append(yp)
    if x == 1:
        yp = yp + 1
        ydata.append(yp)
        xdata.append(xp)
    if x == 3:
        yp = yp - 1
        ydata.append(yp)
        xdata.append(xp)
#    print('yposition',yp)
#    print('xposition',xp,'\n')

#print(xdata,ydata)


#if len(xdata) > len(ydata):
#    xdata = xdata
     
fig, ax = plt.subplots()
ax.plot(xdata,ydata)

ax.set(title='random walk')
ax.grid()

fig.savefig("test.png")
plt.show()