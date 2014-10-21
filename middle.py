# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:26:19 2014

@author: Ozkan
"""

def middle(l):
    """takes a list and returns a new list that contains
    all but the first and last elements."""
    if not isinstance(l,list):
        print 'The input argument must be a list of integers'
        return None
    if len(l)>2:
        l.pop(-1)
        l.pop(0)
    return l
    
def chop(l):
    middle(l)
    return None