# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:54:33 2014

@author: asus
"""
from math import sqrt
def hypotenuse(x,y):
    h=sqrt(x**2+y**2)
    return h
    
if __name__=="__main__":
    h=hypotenuse(3,4)