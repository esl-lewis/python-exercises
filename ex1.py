# -*- coding: utf-8 -*-
import math 
import random


#def buffon(l,t,n):
n = 21300
#n should be a multiple of 213 and l/t = 5/6 for nice results
l = 10
t = 12
h = 0
    # where l is length of needle and t is width of plank
    # t must be larger than l for pi approximation to work, says wikipedia
    # n is total number of needles thrown
for needle in range(1,n+1):
    print('needle',needle)
    
    # h is number of needles that cross line
    
    #randomise position of needle, p is midpoint
    p = random.randint(0,2*t)
    
    print('position',p)
    
    #randomise orientation of needle 
    #where theta is angle from x axis
    theta = random.randint(0, 180)
    #in degrees as feels like cheating to use pi
    #convert from degrees to rads as that is what function works in
    
    
    print('degree',theta)
    
    angle = math.radians(theta)
    
    print('radian',angle)
    
    #use trig to find projection onto x acis
    x = math.cos(angle) * l 
    x = abs(x)
    print('length',x)
    
    start = p - x/2
    end = p + x/2
    #these are start and end points of needle
    print('start', start)
    print('end', end )
    
    if start <= 0 <=end:
        h = h+1
    if start <= t <=end:
        h = h+1 
    if start <= 2*t <=end:
        h = h+1 
    
    print(h)    

pi = (2*l*n) / (t*h)
print('pi',pi)     