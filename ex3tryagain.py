##start again

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ex3


def plot2D(x, y, p):
    fig = plt.figure(figsize=(11,7), dpi=100) #figure is useful for having
    #things like labels,axes etc. 
    ax = fig.gca(projection='3d') #makes axes 3D
    X, Y = np.meshgrid(x, y) #makes grid out of x and y values
    ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=plt.cm.viridis,
                           linewidth=0, antialiased=False)
    #makes a pretty 3D surface
    
    ax.set_xlim(0, 2)   #sets limits of x-axis
    ax.set_ylim(0, 1)   #sets limits of y-axis
    ax.view_init(30, 225)
    ax.set_xlabel('$x$') #labels x-axis
    ax.set_ylabel('$y$') #labels y-axis
# plot2D function takes x-vector y-vector and p-matrix as arguments    


def laplace2d(p, y, dx, dy, l1norm_target): 
    #fnc will iterate until the difference from one iteration to 
    #another of the L1 norm of p meets a specified target
    #l1norm_target is that target
    #also known as taxicab norm, distance between two points as sum of absolute
    #differences in their cartesian coords, zigzags
    
    l1norm = 1 # set start of l1norm
    pn = np.empty_like(p) # empty_like returns a new array the same shape and type as p
    
    while l1norm > l1norm_target:
        pn = p.copy()
        p[1:-1, 1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) +
                         dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) /
                        (2 * (dx**2 + dy**2)))
        #we get the above fnc from discretising the 2nd order derivatives then rearranging
        
        # boundary conditions, I think if we don't keep declaring them here 
        #then the code will start changing them
        p[:, 0] = 0  # p = 0 @ x = 0
        #p[:, -1] = y  # p = y @ x = 2
        p[:, -1] = 1
        p[:, 0] = 0
        p[-1, :] = 0
        p[0, :] = 0
        #p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
        #p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1
        l1norm = (np.sum(np.abs(p[:]) - np.abs(pn[:])) /
                np.sum(np.abs(pn[:])))
        #eq that defines/recalculates l1 norm
     
    return p


if __name__ == '__main__' :
   """##variable declarations
   nx = 31 # number of x points we wish to calculate
   ny = 31 # number of y points we wish to calculate
   dx = 2 / (nx - 1) #is the distance between any pair of adjacent x points
   dy = 2 / (ny - 1) #is the distance between any pair of adjacent y points

   ##initial conditions
   p = np.zeros((ny, nx))  # create a XxY vector of 0's to initialise, 
                        # we start with p=0 everywhere save x=2


   ##plotting aids
   x = np.linspace(0, 2, nx) #for x-axis setup, puts nx number of points between 
                          # 0 and 2
   y = np.linspace(0, 1, ny) #for y-axis setup

   ##boundary conditions 
   p[:, 0] = 0  # p = 0 @ x = 0
   #p[:, -1] = y  # p = y @ x = 2
   p[:, -1] = 1  # heat source, move around
   p[:, 0] = 0
   p[-1, :] = 0
   p[0, :] = 0
   #p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
   #p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1    
   p = laplace2d(p, y, dx, dy, 1e-3)
   plot2D(x, y, p)
   """
   ex3.makejunk(1,2)