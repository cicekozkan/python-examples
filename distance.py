# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:57:07 2014

@author: asus
"""

from math import sqrt

def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    d=sqrt(dsquared)
    return d