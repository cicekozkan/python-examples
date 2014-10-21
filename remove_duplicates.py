# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 20:03:15 2014

@author: cicek
"""

def remove_duplicates(t):
    """takes a list and returns a new
    list with only the unique elements from the original"""
    n = t[:]
    r = []
    for i in range(len(t)):
        n.pop(0)        
        if t[i] not in n:
            r.append(t[i])
    return r