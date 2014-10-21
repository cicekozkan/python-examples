# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 19:59:34 2014

@author: Ozkan
"""

def cumulative_sum(t):
    """takes a list of numbers and returns the cumulative sum; that
    is, a new list where the ith element is the sum of the first i + 1 
    elements from the original list. For example, the cumulative sum of 
    [1, 2, 3] is [1, 3, 6]."""
    res = []
    if not isinstance(t,list):
        print 'The input argument must be a list of integers'
        return None
    for i in range(len(t)):
        if not isinstance(t[i],int):
            print 'The input argument must be a list of integers'
            return None
        res.append(sum(t[:i+1]))
    return res
        
