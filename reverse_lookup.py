# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 21:52:02 2014

@author: ozkan
"""

def reverse_lookup(d, v):
    """gets a dictionary and a value and returns a list of keys that 
    map to v contains
    d: dictionary
    v: value"""
    l=[]
    for k in d:
        if d[k] == v:
            l.append(k)
    return l