# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 16:53:57 2014

@author: Ozkan
"""

def nested_sum(l):
    """takes a nested list of integers and add up
    the elements from all of the nested lists."""
    if not isinstance(l,list):
        print 'The input argument must be a list'
        return None
    total = 0
    for i in l:
        if isinstance(i,list):
            total += nested_sum(i)
        else:
            total += i
    return total
            