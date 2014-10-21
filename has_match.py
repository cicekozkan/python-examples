# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 23:36:56 2014

@author: asus
"""

def has_match(t1, t2):
    """an example function that traverses a list of tuples
    in a for loop and returns true if an index exists such that
    t1[i]==t2[i]
    
    the list of tuples is created with built-in function zip.
    """
    for x, y in zip(t1, t2):    #x,y is a tuple assignment
        if x == y:              
            return True
    return False