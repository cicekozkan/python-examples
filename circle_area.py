# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:00:20 2014

@author: asus
"""
from math import sqrt
from math import pi

def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    d=sqrt(dsquared)
    return d
    
def area(radius):
    return pi*radius**2

def circle_area(xc,yc,xp,yp):
    r=distance(xc,yc,xp,yp)
    a=area(r)
    return a
    