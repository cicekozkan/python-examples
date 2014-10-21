# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 22:14:36 2014

@author: Ozkan
"""
from math import sqrt

def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)


def estimate_pi():
    sum = 0
    k=0
    factor=2*sqrt(2)/9801
    while True:
        n=factorial(4.0*k)*(1103.0+26390.0*k)
        d=(factorial(k)**4.0)*(396.0**(4.0*k))
        r=factor*n/d
        sum=sum + r
        if (abs(r)<1e-15):break
        k=k+1
    return 1/sum