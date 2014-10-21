# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 17:57:21 2014

@author: cicek
"""

def byteArrayToBitArray(bl,size):
    """bl: byte list"""
    t=bl[:]
    r=[]
    for i in range(size):
        while t[i]/2>=2:
            r.append(t[i]%2)
            t[i]/=2
        r.append(t[i]%2)
        r.append(t[i]/2)
    return r
            
            